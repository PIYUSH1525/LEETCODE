class Solution:
    def solve(self, l, r):
        L = 1  
        S = 1  
        steps = 0

        while L <= r:
            R = 4 * L - 1 

            start = max(L, l)
            end = min(R, r)

            if start <= end:
                steps += (end - start + 1) * S

            S += 1
            L = L * 4

        return steps
    def minOperations(self, queries):
        result = 0

        for query in queries:
            l = query[0]
            r = query[1]

            steps = self.solve(l, r)
            result += (steps + 1) // 2
        return result