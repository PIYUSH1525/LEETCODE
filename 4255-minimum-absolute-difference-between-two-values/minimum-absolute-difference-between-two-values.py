class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        diff = float('inf')
        if 1 not in nums or 2 not in nums:
            return -1
        for i in range(n):
            for j in range(n):
                if nums[i]==1 and nums[j] ==2:
                    diff = min(abs(i-j),diff)
        return diff