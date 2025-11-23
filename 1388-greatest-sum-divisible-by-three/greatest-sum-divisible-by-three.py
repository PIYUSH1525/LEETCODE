class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-float('inf')] * 3 for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            current_num = nums[i - 1]
            for remainder in range(3):
                dp[i][remainder] = dp[i - 1][remainder]
                prev_remainder = (remainder - current_num) % 3
                dp[i][remainder] = max(
                    dp[i][remainder], 
                    dp[i - 1][prev_remainder] + current_num
                )
        return dp[n][0]