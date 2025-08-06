class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        self.n = len(baskets)
        self.seg = [0] * (4 * self.n)
        self._build(baskets, 0, self.n - 1, 1)

        unplaced = 0
        for f in fruits:
            if self._find_and_use(f, 0, self.n - 1, 1) == -1:
                unplaced += 1
        return unplaced

    def _build(self, baskets: List[int], low: int, high: int, idx: int):
        if low == high:
            self.seg[idx] = baskets[low]
        else:
            mid = (low + high) // 2
            self._build(baskets, low, mid, idx * 2)
            self._build(baskets, mid + 1, high, idx * 2 + 1)
            self.seg[idx] = max(self.seg[idx * 2], self.seg[idx * 2 + 1])

    def _find_and_use(self, fruit: int, low: int, high: int, idx: int) -> int:
        if self.seg[idx] < fruit:
            return -1
        if low == high:
            self.seg[idx] = -1
            return 1
        mid = (low + high) // 2
        if self.seg[idx * 2] >= fruit:
            res = self._find_and_use(fruit, low, mid, idx * 2)
        else:
            res = self._find_and_use(fruit, mid + 1, high, idx * 2 + 1)
        self.seg[idx] = max(self.seg[idx * 2], self.seg[idx * 2 + 1])
        return res
        