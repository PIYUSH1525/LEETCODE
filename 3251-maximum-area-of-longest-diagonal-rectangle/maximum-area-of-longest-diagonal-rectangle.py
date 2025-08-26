import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_diag_squared = 0
        max_area = 0

        for l, w in dimensions:
            diag_squared = l**2 + w**2
            area = l * w

            if diag_squared > max_diag_squared:
                max_diag_squared = diag_squared
                max_area = area
            elif diag_squared == max_diag_squared:
                max_area = max(max_area, area)

        return max_area