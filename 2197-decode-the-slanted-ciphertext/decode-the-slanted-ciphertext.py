class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        result = []
        cols = len(encodedText) // rows
        for start_col in range(cols):
            row_pos = 0
            col_pos = start_col
            while row_pos < rows and col_pos < cols:
                index = row_pos * cols + col_pos
                result.append(encodedText[index])
                row_pos += 1
                col_pos += 1
        return ''.join(result).rstrip()