from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        while queue:
            current_index = queue.popleft()
            if arr[current_index] == 0:
                return True
            jump_distance = arr[current_index]
            arr[current_index] = -1
            for next_index in (current_index + jump_distance, current_index - jump_distance):
                if 0 <= next_index < len(arr) and arr[next_index] >= 0:
                    queue.append(next_index)
        return False
