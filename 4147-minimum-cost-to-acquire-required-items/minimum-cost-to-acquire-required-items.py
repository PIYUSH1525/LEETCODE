from typing import List, Optional
class Solution:
    def minimumCost(self,cost1:int,cost2:int,costBoth:int,need1:int,need2:int)->int:
        together=min(need1,need2)
        return (together*min(costBoth,cost1+cost2)+
                max(0,need1-need2)*min(cost1,costBoth)+
                max(0,need2-need1)*min(cost2,costBoth))