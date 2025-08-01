class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            new_row = [1]
            for j in range(1, i):
                sum_of_element = res[i - 1][j - 1] + res[i - 1][j]
                new_row.append(sum_of_element)
            new_row.append(1)
            res.append(new_row)
        return res