class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxx = nums[0]
        res = 0
        for i in range(len(nums)):
            if nums[i] > maxx:
                maxx =nums[i]
                res = i
        return res
