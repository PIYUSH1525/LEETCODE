class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        last_significant_number_index = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] > nums[last_significant_number_index] and nums[i] > nums[i + 1]:
                count += 1
            elif nums[i] < nums[last_significant_number_index] and nums[i] < nums[i + 1]:
                count += 1
            last_significant_number_index = i
        return count