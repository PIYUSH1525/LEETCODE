class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        diff = 0
        nums.sort()
        if len(nums)<2:
            return 0
        i = 0 
        j = 1
        while j < len(nums):
            d = nums[j]-nums[i]
            diff = max(diff,d)
            i+=1
            j+=1
        return diff
        