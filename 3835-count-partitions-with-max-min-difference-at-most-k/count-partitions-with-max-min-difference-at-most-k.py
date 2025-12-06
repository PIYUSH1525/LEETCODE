class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        sorted_window = SortedList()
        n = len(nums)
        dp = [1] + [0] * n
        prefix_sum = [1] + [0] * n
        left = 1
      
        for right in range(1, n + 1):
            sorted_window.add(nums[right - 1])
          
            while sorted_window[-1] - sorted_window[0] > k:
                sorted_window.remove(nums[left - 1])
                left += 1
            if left >= 2:
                dp[right] = (prefix_sum[right - 1] - prefix_sum[left - 2] + MOD) % MOD
            else:
                dp[right] = prefix_sum[right - 1] % MOD
            prefix_sum[right] = (prefix_sum[right - 1] + dp[right]) % MOD
      
        return dp[n]