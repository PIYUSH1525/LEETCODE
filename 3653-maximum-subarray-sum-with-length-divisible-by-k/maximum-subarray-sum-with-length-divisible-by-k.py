class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        min_prefix_sum = [float('inf')] * k
        max_sum = float('-inf')
        prefix_sum = 0
        min_prefix_sum[-1] = 0
        for index, value in enumerate(nums):
            prefix_sum += value
            remainder = index % k
            max_sum = max(max_sum, prefix_sum - min_prefix_sum[remainder])
            min_prefix_sum[remainder] = min(min_prefix_sum[remainder], prefix_sum)      
        return max_sum
