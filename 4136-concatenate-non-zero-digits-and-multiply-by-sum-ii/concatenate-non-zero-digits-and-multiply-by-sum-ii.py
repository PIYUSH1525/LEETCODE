class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        p = [1] * (n + 1)
        for i in range(1, n + 1): p[i] = p[i-1] * 10 % MOD

        pre = [0] * (n + 1)
        for i in range(n): pre[i+1] = pre[i] + int(s[i])

        st = [(0, 0)] * (2 * n)
        for i in range(n):
            st[n + i] = (0, 0) if s[i] == '0' else (int(s[i]), 1)

        def merge(a, b):
            return (a[0] * p[b[1]] + b[0]) % MOD, a[1] + b[1]

        for i in range(n - 1, 0, -1):
            st[i] = merge(st[i << 1], st[i << 1 | 1])

        ans = []
        for ql, qr in queries:
            l, r = ql + n, qr + n + 1
            L, R = (0, 0), (0, 0)
            while l < r:
                if l & 1: L = merge(L, st[l]); l += 1
                if r & 1: r -= 1; R = merge(st[r], R)
                l >>= 1; r >>= 1
            x = merge(L, R)
            ans.append(x[0] * (pre[qr + 1] - pre[ql]) % MOD)

        return ans