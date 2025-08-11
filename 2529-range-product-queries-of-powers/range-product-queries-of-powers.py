class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = int(1e9 + 7)
        powers = []
        result = []
        for i in range(32):
            if (n >> i) & 1:
                powers.append(1 << i)
        for query in queries:
            start = query[0]
            end = query[1]

            product = 1
            for i in range(start, end + 1):
                product = (product * powers[i]) % MOD
            result.append(product)
        return result