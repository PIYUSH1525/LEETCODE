class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total_cost = sum(cost) - sum(cost[2::3])
      
        return total_cost