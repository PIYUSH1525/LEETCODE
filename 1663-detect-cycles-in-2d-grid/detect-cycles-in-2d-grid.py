class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        parent = list(range(m * n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return True
            parent[ra] = rb
            return False

        for i in range(m):
            for j in range(n):
                if j + 1 < n and grid[i][j] == grid[i][j+1]:
                    if union(i*n+j, i*n+j+1):
                        return True
                if i + 1 < m and grid[i][j] == grid[i+1][j]:
                    if union(i*n+j, (i+1)*n+j):
                        return True
        return False