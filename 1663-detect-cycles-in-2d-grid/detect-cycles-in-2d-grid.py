class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for start_row in range(rows):
            for start_col in range(cols):
                if visited[start_row][start_col]:
                    continue
                visited[start_row][start_col] = True
                stack = [(start_row, start_col, -1, -1)]
                while stack:
                    curr_row, curr_col, parent_row, parent_col = stack.pop()
                    for delta_row, delta_col in directions:
                        next_row = curr_row + delta_row
                        next_col = curr_col + delta_col
                        if 0 <= next_row < rows and 0 <= next_col < cols:
                            if (grid[next_row][next_col] != grid[start_row][start_col] or 
                                (next_row == parent_row and next_col == parent_col)):
                                continue
                            if visited[next_row][next_col]:
                                return True
                            visited[next_row][next_col] = True
                            stack.append((next_row, next_col, curr_row, curr_col))
      
        return False