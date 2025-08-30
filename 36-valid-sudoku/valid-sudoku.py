class Solution:
    def isValidSudoku(self, board):
        st = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                row = board[i][j] + "_row_" + str(i)
                col = board[i][j] + "_col_" + str(j)
                box = board[i][j] + "_box_" + str(i // 3) + "_" + str(j // 3)
                if row in st or col in st or box in st:
                    return False
                st.add(row)
                st.add(col)
                st.add(box)
        
        return True