class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        current_rotation_value = sum(index * value for index, value in enumerate(nums))
        array_length = len(nums)
        total_sum = sum(nums)
        max_rotation_value = current_rotation_value
        for rotation in range(1, array_length):
            current_rotation_value = current_rotation_value + total_sum - array_length * nums[array_length - rotation]
            max_rotation_value = max(max_rotation_value, current_rotation_value)
      
        return max_rotation_value