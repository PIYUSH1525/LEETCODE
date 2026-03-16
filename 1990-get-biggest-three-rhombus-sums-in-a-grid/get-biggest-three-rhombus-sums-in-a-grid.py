class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        diagonal_sum_down_right = [[0] * (cols + 2) for _ in range(rows + 1)]
        diagonal_sum_down_left = [[0] * (cols + 2) for _ in range(rows + 1)]
        for i, row in enumerate(grid, 1):
            for j, value in enumerate(row, 1):
                diagonal_sum_down_right[i][j] = diagonal_sum_down_right[i - 1][j - 1] + value
                diagonal_sum_down_left[i][j] = diagonal_sum_down_left[i - 1][j + 1] + value
        unique_sums = SortedSet()
        for i, row in enumerate(grid, 1):
            for j, center_value in enumerate(row, 1):
                max_radius = min(i - 1, rows - i, j - 1, cols - j)
                unique_sums.add(center_value)
                for radius in range(1, max_radius + 1):
                    top_right_edge = diagonal_sum_down_right[i + radius][j] - diagonal_sum_down_right[i][j - radius]
                    bottom_right_edge = diagonal_sum_down_right[i][j + radius] - diagonal_sum_down_right[i - radius][j]
                    top_left_edge = diagonal_sum_down_left[i][j - radius] - diagonal_sum_down_left[i - radius][j]
                    bottom_left_edge = diagonal_sum_down_left[i + radius][j] - diagonal_sum_down_left[i][j + radius]
                    rhombus_sum = (top_right_edge + bottom_right_edge + top_left_edge + bottom_left_edge 
                                  - grid[i + radius - 1][j - 1] + grid[i - radius - 1][j - 1])
                  
                    unique_sums.add(rhombus_sum)
                while len(unique_sums) > 3:
                    unique_sums.remove(unique_sums[0]) 
        return list(unique_sums)[::-1]