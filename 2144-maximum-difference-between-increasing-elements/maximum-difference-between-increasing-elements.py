class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l = 0
        r = 1
        maxx = -1
        while r < len(nums):
            if nums[l] < nums[r]:
                diff = nums[r] - nums[l]
                maxx = max(maxx,diff)
            else:
                l =r
            r+=1
        return maxx
