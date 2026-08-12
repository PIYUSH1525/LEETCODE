from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency_map = defaultdict(int)
        max_length = 0
        left = 0
        for right, current_num in enumerate(nums):
            frequency_map[current_num] += 1
          
            while frequency_map[current_num] > k:
                frequency_map[nums[left]] -= 1
                left += 1
    
            max_length = max(max_length, right - left + 1)
      
        return max_length