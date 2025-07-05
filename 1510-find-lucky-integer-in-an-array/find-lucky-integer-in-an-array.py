class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = [-1]
        s = Counter(arr)
        for key,val in s.items():
            if key == val:
                res.append(val)
        return max(res)
