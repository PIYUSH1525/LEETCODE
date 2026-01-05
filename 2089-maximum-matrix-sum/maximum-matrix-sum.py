class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_absolute_value = float('inf')
        total_absolute_sum = 0
        negative_count = 0
        for row in matrix:
            for value in row:
                if value < 0:
                    negative_count += 1
                absolute_value = abs(value)
                min_absolute_value = min(min_absolute_value, absolute_value)
                total_absolute_sum += absolute_value
        if negative_count % 2 == 0:
            return total_absolute_sum
        else:
            return total_absolute_sum - 2 * min_absolute_value