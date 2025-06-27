class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        c = Counter(nums)
        for key , value in c.items():
            if value> 1:
                res.append(key)
        return res
        