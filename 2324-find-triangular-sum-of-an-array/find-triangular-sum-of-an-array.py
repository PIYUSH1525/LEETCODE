class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for current_length in range(len(nums) - 1, 0, -1):
            for i in range(current_length):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        return nums[0]