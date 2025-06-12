class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        N = len(nums)
        nums.append(nums[0])
        return max(abs(nums[i] - nums[i+1]) for i in range(N))
        # n = len(nums)
        # max_diff = 0
        # for i in range(n):
        #     diff = abs(nums[i] - nums[(i + 1) % n])
        #     max_diff = max(max_diff, diff)
        # return max_diff