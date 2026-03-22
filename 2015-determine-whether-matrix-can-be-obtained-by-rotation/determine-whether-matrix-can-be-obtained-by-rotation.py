class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
      
        def rotate_90_clockwise(matrix: List[List[int]]) -> None:
            n = len(matrix)
            for layer in range(n // 2):
                first = layer
                last = n - 1 - layer
                for i in range(first, last):
                    offset = i - first
                    temp = matrix[first][i]
                    matrix[first][i] = matrix[last - offset][first]
                    matrix[last - offset][first] = matrix[last][last - offset]
                    matrix[last][last - offset] = matrix[i][last]
                    matrix[i][last] = temp
        for rotation_count in range(4):
            if mat == target:
                return True
            rotate_90_clockwise(mat)
        return False