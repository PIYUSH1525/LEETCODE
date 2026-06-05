class Solution:
    def totalWaviness(self, l: int, r: int) -> int:
        from functools import lru_cache

        def solve(n: int) -> int:
            s = str(n)

            @lru_cache(maxsize=None)
            def dfs(i, a, b, tight, started, length):
                if i == len(s):
                    return (1, 0)

                limit = int(s[i]) if tight else 9
                cnt = wav = 0

                for d in range(0, limit + 1):
                    new_tight   = tight and d == int(s[i])
                    new_started = started or d > 0
                    new_len     = (length + 1) if new_started else 0

                    c, w = dfs(i + 1, b, d, new_tight, new_started, new_len)

                    if length > 1 and ((a < b > d) or (a > b < d)):
                        w += c

                    cnt += c
                    wav += w

                return (cnt, wav)

            return dfs(0, 0, 0, True, False, 0)[1]

        return solve(r) - solve(l - 1)