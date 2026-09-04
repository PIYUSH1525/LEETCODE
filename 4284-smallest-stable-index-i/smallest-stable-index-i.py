class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)

        max_prev = [0] * n
        min_next = [0] * n

        max_prev[0] = nums[0]
        for i in range(1, n):
            max_prev[i] = max(max_prev[i - 1], nums[i])

        min_next[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            min_next[i] = min(min_next[i + 1], nums[i])

        for i in range(n):
            if max_prev[i] - min_next[i] <= k:
                return i

        return -1