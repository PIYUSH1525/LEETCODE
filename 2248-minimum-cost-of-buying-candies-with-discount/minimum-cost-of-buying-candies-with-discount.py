class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        res=0
        took=0
        for i in range(len(cost)-1,-1,-1):
            if took==2:
                took=0
            else:
                res+=cost[i]
                took+=1
        return res
        