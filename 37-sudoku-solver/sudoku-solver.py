class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def backtrack(index):
            nonlocal solved
            if index == len(empty_cells):
                solved = True
                return
            row_idx, col_idx = empty_cells[index]
            for digit in range(9):
                if (not row_used[row_idx][digit] and 
                    not col_used[col_idx][digit] and 
                    not block_used[row_idx // 3][col_idx // 3][digit]):
                    row_used[row_idx][digit] = True
                    col_used[col_idx][digit] = True
                    block_used[row_idx // 3][col_idx // 3][digit] = True
                    board[row_idx][col_idx] = str(digit + 1)
                    backtrack(index + 1)
                    if solved:
                        return
                    row_used[row_idx][digit] = False
                    col_used[col_idx][digit] = False
                    block_used[row_idx // 3][col_idx // 3][digit] = False
        row_used = [[False] * 9 for _ in range(9)]
        col_used = [[False] * 9 for _ in range(9)]
        block_used = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        empty_cells = []
        solved = False
        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] == '.':
                    empty_cells.append((row_idx, col_idx))
                else:
                    digit = int(board[row_idx][col_idx]) - 1
                    row_used[row_idx][digit] = True
                    col_used[col_idx][digit] = True
                    block_used[row_idx // 3][col_idx // 3][digit] = True
        backtrack(0)