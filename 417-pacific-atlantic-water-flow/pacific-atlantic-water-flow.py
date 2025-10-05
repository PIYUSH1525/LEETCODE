from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      
        def bfs(queue: deque, visited: set) -> None:
            while queue:
                level_size = len(queue)
                for _ in range(level_size):
                    curr_row, curr_col = queue.popleft()
                    directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
                    for delta_row, delta_col in directions:
                        next_row = curr_row + delta_row
                        next_col = curr_col + delta_col
                        if (0 <= next_row < rows and 
                            0 <= next_col < cols and 
                            (next_row, next_col) not in visited and 
                            heights[next_row][next_col] >= heights[curr_row][curr_col]):
                          
                            visited.add((next_row, next_col))
                            queue.append((next_row, next_col))
      
        rows = len(heights)
        cols = len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        pacific_queue = deque()
        atlantic_queue = deque()
        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    pacific_visited.add((row, col))
                    pacific_queue.append((row, col))
                if row == rows - 1 or col == cols - 1:
                    atlantic_visited.add((row, col))
                    atlantic_queue.append((row, col))
      
        bfs(pacific_queue, pacific_visited)
        bfs(atlantic_queue, atlantic_visited)
      
        result = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific_visited and (row, col) in atlantic_visited:
                    result.append([row, col])
      
        return result