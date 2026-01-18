class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        col_prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                row_prefix_sum[i][j] = row_prefix_sum[i][j - 1] + grid[i - 1][j - 1]
                col_prefix_sum[i][j] = col_prefix_sum[i - 1][j] + grid[i - 1][j - 1]

        def is_magic_square(top_row: int, left_col: int, bottom_row: int, right_col: int) -> bool:
            target_sum = row_prefix_sum[top_row + 1][right_col + 1] - row_prefix_sum[top_row + 1][left_col]
            for row in range(top_row + 1, bottom_row + 1):
                row_sum = row_prefix_sum[row + 1][right_col + 1] - row_prefix_sum[row + 1][left_col]
                if row_sum != target_sum:
                    return False
            for col in range(left_col, right_col + 1):
                col_sum = col_prefix_sum[bottom_row + 1][col + 1] - col_prefix_sum[top_row][col + 1]
                if col_sum != target_sum:
                    return False
            main_diagonal_sum = 0
            row, col = top_row, left_col
            while row <= bottom_row:
                main_diagonal_sum += grid[row][col]
                row += 1
                col += 1
            if main_diagonal_sum != target_sum:
                return False
            anti_diagonal_sum = 0
            row, col = top_row, right_col
            while row <= bottom_row:
                anti_diagonal_sum += grid[row][col]
                row += 1
                col -= 1
            if anti_diagonal_sum != target_sum:
                return False
          
            return True
        for square_size in range(min(rows, cols), 1, -1):
            for start_row in range(rows - square_size + 1):
                for start_col in range(cols - square_size + 1):
                    end_row = start_row + square_size - 1
                    end_col = start_col + square_size - 1
                  
                    if is_magic_square(start_row, start_col, end_row, end_col):
                        return square_size
        return 1