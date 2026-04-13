class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                curr= abs(i - start)
                res = min(res,curr)
        return res