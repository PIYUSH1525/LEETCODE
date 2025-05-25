class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        maxx = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit =  prices[r] - prices[l]
                maxx = max(profit, maxx)

            else:
                l =r 
            r+=1
        return maxx
        

        # max_profit = 0
        # n = len(prices)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         max_profit = max(max_profit, prices[j]-prices[i])
        # return max_profit



        