class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        min_heap = []
        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    heappush(min_heap, (heightMap[row][col], row, col))
                    visited[row][col] = True
        total_water = 0
        directions = (-1, 0, 1, 0, -1)
        while min_heap:
            current_height, current_row, current_col = heappop(min_heap)
            for i in range(4):
                next_row = current_row + directions[i]
                next_col = current_col + directions[i + 1]
                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    not visited[next_row][next_col]):
                    total_water += max(0, current_height - heightMap[next_row][next_col])
                  
                    visited[next_row][next_col] = True
                    heappush(min_heap, (max(current_height, heightMap[next_row][next_col]), 
                                       next_row, next_col))
      
        return total_water