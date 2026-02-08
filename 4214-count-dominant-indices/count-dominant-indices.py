class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        def solve(i, s_sum, s_count):
            if i < 0:
                return 0
            is_dominant = 0
            if s_count > 0 and nums[i] > (s_sum / s_count):
                is_dominant = 1
            return is_dominant + solve(i - 1, s_sum + nums[i], s_count + 1)
        return solve(n - 2, nums[n - 1], 1)