from typing import List
from bisect import bisect_left
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        triangle_count = 0
        array_length = len(nums)
        for first_side_idx in range(array_length - 2):
            for second_side_idx in range(first_side_idx + 1, array_length - 1):
                sum_of_two_sides = nums[first_side_idx] + nums[second_side_idx]
                insertion_point = bisect_left(nums, sum_of_two_sides, lo=second_side_idx + 1)
                largest_valid_idx = insertion_point - 1
                triangle_count += largest_valid_idx - second_side_idx
      
        return triangle_count