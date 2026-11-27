class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = [0]*n
        for i in range(n):
            fac = items[i][0]
            for j in range(n):
                if i !=j and items[j][0] % fac == 0:
                    bonus[i] += 1
        dp = [0]*(budget+1)
        for i in range(1, n+1):
            price = items[i-1][1]
            extra = bonus[i-1]
            for j in range(budget, price-1, -1):
                if j-price==0 or dp[j-price]>0:
                    dp[j] = max(dp[j], dp[j-price]+extra+1)

            for j in range(price, budget+1):
                if dp[j-price]>0:
                    dp[j] = max(dp[j], dp[j-price]+1)
        return max(dp)