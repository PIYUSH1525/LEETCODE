class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        T = [[0] * k for _ in range(2*n)]
        P = [0] * (2*n)
        
        def update(i, r):
            i += n
            T[i] = [0] * k
            T[i][r] = 1 ; P[i] = r
            i>>=1
            while i:
                T[i] = T[(i<<1)][:]
                P[i] = P[(i<<1)] * P[(i<<1) + 1] % k
                for j in range(k):
                    T[i][P[(i<<1)]*j % k] += T[(i<<1) + 1][j]
                i>>=1

        for i in range(n): 
            r = nums[i] % k
            T[i+n][r] = 1
            P[i+n] = r
        for i in range(n-1, 0, -1):
            T[i] = T[(i<<1)][:]
            P[i] = P[(i<<1)] * P[(i<<1) + 1] % k
            for j in range(k):
                T[i][P[(i<<1)]*j % k] += T[(i<<1) + 1][j]

        def nodes(l, r):
            l+=n; r+=n
            L, R = [], []
            while l <= r:
                if l&1:
                    L.append(l)
                    l += 1
                if r&1 == 0:
                    R.append(r)
                    r -= 1
                l>>=1;r>>=1
            return L + R[::-1]
            
        def query(l, r, x):
            ans = [0] * k
            prefix = 1
            U = nodes(l, r)
            for u in U:
                for j in range(k):
                    ans[prefix * j % k] += T[u][j]
                prefix = prefix * P[u] % k
            return ans[x]

        A = []
        for i, v, s, x in queries:
            update(i, v % k)
            A.append(query(s, n-1, x))
        return A