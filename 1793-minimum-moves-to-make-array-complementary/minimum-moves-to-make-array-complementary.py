from typing import List
from itertools import accumulate
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        diff_array = [0] * (2 * limit + 2)
        n = len(nums)
        for i in range(n // 2):
            left_val = nums[i]
            right_val = nums[n - 1 - i]
            if left_val > right_val:
                left_val, right_val = right_val, left_val
            diff_array[2] += 2
            diff_array[left_val + 1] -= 2
            diff_array[left_val + 1] += 1
            diff_array[left_val + right_val] -= 1
            diff_array[left_val + right_val + 1] += 1
            diff_array[right_val + limit + 1] -= 1
            diff_array[right_val + limit + 1] += 2
        return min(accumulate(diff_array[2:]))