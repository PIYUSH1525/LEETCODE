class Solution:
    def countSubarraysOfOnes(self, row_mask: list[int]) -> int:
        consecutive_ones = 0
        subarray_count = 0
        for val in row_mask:
            if val == 0:
                consecutive_ones = 0
            else:
                consecutive_ones += 1
            subarray_count += consecutive_ones
        return subarray_count
    def numSubmat(self, mat: list[list[int]]) -> int:
        if not mat or not mat[0]:
            return 0  
        rows = len(mat)
        cols = len(mat[0])
        total_count = 0
        for top_row in range(rows):
            row_mask = [1] * cols
            for bottom_row in range(top_row, rows):
                for col in range(cols):
                    row_mask[col] &= mat[bottom_row][col]
                total_count += self.countSubarraysOfOnes(row_mask)
        return total_count