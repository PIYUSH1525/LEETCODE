from typing import List
from math import inf

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_element = nums[0]
        smallest = inf
        second_smallest = inf
        for current_num in nums[1:]:
            if current_num < smallest:
                second_smallest = smallest
                smallest = current_num
            elif current_num < second_smallest:
                second_smallest = current_num
        return first_element + smallest + second_smallest