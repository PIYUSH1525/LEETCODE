class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * 101 for _ in range(101)]
        tower[0][0] = float(poured)
        for row in range(query_row + 1):
            for col in range(row + 1):
                if tower[row][col] > 1.0:
                    overflow = tower[row][col] - 1.0
                    tower[row][col] = 1.0
                    tower[row + 1][col] += overflow / 2.0
                    tower[row + 1][col + 1] += overflow / 2.0
        return min(1.0, tower[query_row][query_glass])