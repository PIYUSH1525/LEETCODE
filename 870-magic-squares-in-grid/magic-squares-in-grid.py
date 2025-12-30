class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_square(row: int, col: int) -> int:
            if row + 3 > rows or col + 3 > cols:
                return 0
            unique_numbers = set()
            row_sums = [0] * 3
            col_sums = [0] * 3
            main_diagonal_sum = 0
            anti_diagonal_sum = 0
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    value = grid[i][j]
                    if value < 1 or value > 9:
                        return 0
                    unique_numbers.add(value)
                    relative_row = i - row
                    relative_col = j - col
                    row_sums[relative_row] += value
                    col_sums[relative_col] += value
                    if relative_row == relative_col:
                        main_diagonal_sum += value
                    if relative_row == 2 - relative_col:
                        anti_diagonal_sum += value
            if len(unique_numbers) != 9:
                return 0
            if main_diagonal_sum != anti_diagonal_sum:
                return 0
            if any(row_sum != main_diagonal_sum for row_sum in row_sums):
                return 0
            if any(col_sum != main_diagonal_sum for col_sum in col_sums):
                return 0
          
            return 1
        rows, cols = len(grid), len(grid[0])
        return sum(is_magic_square(i, j) for i in range(rows) for j in range(cols))