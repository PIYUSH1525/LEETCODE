class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        dp = [[0] * C for _ in range(R)]

        dp[0][0] = grid[0][0]
        for col in range(1, C):
            dp[0][col] = grid[0][col] ^ dp[0][col - 1]

        for row in range(1, R):
            dp[row][0] = grid[row][0] ^ dp[row - 1][0]

        for row in range(1, R):
            for col in range(1, C):
                dp[row][col] = set()

        for row in range(1, R):
            for col in range(1, C):
                if row - 1 == 0:
                    dp[row][col].add(grid[row][col] ^ dp[row - 1][col])

                if col - 1 == 0:
                    dp[row][col].add(grid[row][col] ^ dp[row][col - 1])

                if col - 1 > 0:
                    for num in dp[row][col - 1]:
                        dp[row][col].add(grid[row][col] ^ num)

                if row - 1 > 0:
                    for num in dp[row - 1][col]:
                        dp[row][col].add(grid[row][col] ^ num)

        if isinstance(dp[R - 1][C - 1], int):
            return dp[R - 1][C - 1]
            
        return min(dp[R - 1][C - 1])