class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wind_sum = sum(nums[0:k])
        max_sum = wind_sum
        for i in range(k, len(nums)):
            wind_sum = wind_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum,wind_sum)
        return max_sum/k

        