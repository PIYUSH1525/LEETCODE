class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        n, m = len(classroom), len(classroom[0])
        x = y = -1
        cnt_litter = 0
        h = {}
        for i in range(n):
            for j in range(m):
                if classroom[i][j] == "S":
                    x, y = i, j
                elif classroom[i][j] == "L":
                    cnt_litter += 1
                    h[(i, j)] = 1 << cnt_litter
        d = [[[0] * (1 << (cnt_litter + 1)) for _ in range(m)] for _ in range(n)]
        curr = [(x, y, energy, cnt_litter, 0)]
        min_moves = 0
        while curr:
            nxt = []
            for x, y, curr_energy, curr_litter, mask in curr:
                if classroom[x][y] == "R":
                    curr_energy = energy
                if classroom[x][y] == "L":
                    t = h[(x, y)]
                    if (mask & t) != t:
                        curr_litter -= 1
                        mask |= t
                if curr_litter == 0:
                    return min_moves
                for i, j in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
                    if 0 <= i < n and 0 <= j < m and classroom[i][j] != "X" and curr_energy and d[i][j][mask] < curr_energy:
                        d[i][j][mask] = curr_energy
                        nxt.append((i, j, curr_energy - 1, curr_litter, mask))
            curr = nxt
            min_moves += 1
        return -1
                
                