class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7
        n = len(edges) + 1
        LOG = (n + 1).bit_length()

        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        up = [[-1] * (n + 1) for _ in range(LOG)]
        dep = [0] * (n + 1)

        def dfs(u, p):
            up[0][u] = p
            for v in g[u]:
                if v != p:
                    dep[v] = dep[u] + 1
                    dfs(v, u)

        dfs(1, -1)

        for k in range(1, LOG):
            for i in range(1, n + 1):
                if up[k - 1][i] != -1:
                    up[k][i] = up[k - 1][up[k - 1][i]]

        def lca(a, b):
            if dep[a] < dep[b]:
                a, b = b, a

            for k in range(LOG - 1, -1, -1):
                if up[k][a] != -1 and dep[up[k][a]] >= dep[b]:
                    a = up[k][a]

            if a == b:
                return a

            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]

            return up[0][a]

        ans = []

        for u, v in queries:
            x = lca(u, v)
            d = dep[u] + dep[v] - 2 * dep[x]
            ans.append(pow(2, d - 1, MOD) if d else 0)

        return ans