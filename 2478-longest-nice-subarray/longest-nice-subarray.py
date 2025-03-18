class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_length = 0
        l =0
        mask = 0
        for r in range(len(nums)):
            while (mask & nums[r] != 0):
                mask ^= nums[l]
                l+=1
            mask |= nums[r]  # putted next digit
            max_length = max(max_length, r - l + 1)
        return max_length
            
        