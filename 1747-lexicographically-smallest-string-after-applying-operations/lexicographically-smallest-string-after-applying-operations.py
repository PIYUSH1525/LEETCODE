from collections import deque
from typing import Set

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        queue = deque([s])
    
        visited: Set[str] = {s}
      
        smallest_string = s
        while queue:
            current_string = queue.popleft()
          
            if smallest_string > current_string:
                smallest_string = current_string
          
            transformed_add = ''.join(
                str((int(char) + a) % 10) if index % 2 == 1 else char 
                for index, char in enumerate(current_string)
            )
          
            transformed_rotate = current_string[-b:] + current_string[:-b]
          
            for transformed in (transformed_add, transformed_rotate):
                if transformed not in visited:
                    visited.add(transformed)
                    queue.append(transformed)
      
        return smallest_string