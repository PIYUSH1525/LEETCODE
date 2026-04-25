class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        a = []
        for x, y in points:
            if x == 0:
                a.append(y)
            elif y == side:
                a.append(side + x)
            elif x == side:
                a.append(side * 3 - y)
            else:
                a.append(side * 4 - x)
        a.sort()

        def check(low: int) -> bool:
            idx = [0] * k
            cur = a[0]
            for j in range(1, k):
                i = bisect_left(a, cur + low)
                if i == len(a):
                    return False
                idx[j] = i
                cur = a[i]
            if cur - a[0] <= side * 4 - low:
                return True
            for idx[0] in range(1, idx[1]):
                for j in range(1, k):
                    while a[idx[j]] < a[idx[j - 1]] + low:
                        idx[j] += 1
                        if idx[j] == len(a):
                            return False
                if a[idx[-1]] - a[idx[0]] <= side * 4 - low:
                    return True
            return False

        left, right = 1, side + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left