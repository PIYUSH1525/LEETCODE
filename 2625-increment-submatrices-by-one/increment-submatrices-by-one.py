class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
    
        for row1, col1, row2, col2 in queries:
            matrix[row1][col1] += 1
          
            if row2 + 1 < n:
                matrix[row2 + 1][col1] -= 1
          
            if col2 + 1 < n:
                matrix[row1][col2 + 1] -= 1
            if row2 + 1 < n and col2 + 1 < n:
                matrix[row2 + 1][col2 + 1] += 1
      
        for row in range(n):
            for col in range(n):
                if row > 0:
                    matrix[row][col] += matrix[row - 1][col]
              
                if col > 0:
                    matrix[row][col] += matrix[row][col - 1]
              
                if row > 0 and col > 0:
                    matrix[row][col] -= matrix[row - 1][col - 1]
      
        return matrix
