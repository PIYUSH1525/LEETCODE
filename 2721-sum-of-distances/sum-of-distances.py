from collections import defaultdict
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        value_to_indices = defaultdict(list)
        for index, value in enumerate(nums):
            value_to_indices[value].append(index)
        result = [0] * len(nums)
        for indices in value_to_indices.values():
            left_sum = 0
            right_sum = sum(indices) - len(indices) * indices[0]
            for i in range(len(indices)):
                result[indices[i]] = left_sum + right_sum
                if i + 1 < len(indices):
                    gap = indices[i + 1] - indices[i]
                    left_sum += gap * (i + 1)
                    right_sum -= gap * (len(indices) - i - 1)
      
        return result