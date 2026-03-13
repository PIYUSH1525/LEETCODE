from typing import List
from math import sqrt

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def can_complete_in_time(time_limit: int) -> bool:
            total_height_reduced = 0

            for worker_time in workerTimes:
                max_rounds = int(sqrt(2 * time_limit / worker_time + 0.25) - 0.5)
                total_height_reduced += max_rounds

            return total_height_reduced >= mountainHeight
        left, right = 1, 10**16
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2
            if can_complete_in_time(mid):
                first_true_index = mid
                right = mid - 1 
            else:
                left = mid + 1  
        return first_true_index