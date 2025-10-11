from typing import List
from collections import Counter
from functools import cache
from bisect import bisect_right


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
      
        @cache
        def calculate_max_damage(index: int) -> int:
            if index >= array_length:
                return 0
          
            skip_current = calculate_max_damage(index + power_count[sorted_power[index]])
          
            current_damage = sorted_power[index] * power_count[sorted_power[index]]
            take_current = current_damage + calculate_max_damage(next_valid_index[index])
          
            return max(skip_current, take_current)
      
        array_length = len(power)
      
        power_count = Counter(power)
      
        sorted_power = sorted(power)
      
        next_valid_index = [
            bisect_right(sorted_power, value + 2, lo=i + 1) 
            for i, value in enumerate(sorted_power)
        ]
      
        return calculate_max_damage(0)
