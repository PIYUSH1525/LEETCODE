class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix_sum = [0] * (n + 1)
        for i, customer in enumerate(customers):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if customer == 'Y' else 0)
        best_hour = 0
        min_penalty = float('inf')
      
        for closing_hour in range(n + 1):
            penalty_before = closing_hour - prefix_sum[closing_hour]
            penalty_after = prefix_sum[-1] - prefix_sum[closing_hour]
          
            total_penalty = penalty_before + penalty_after
            if total_penalty < min_penalty:
                best_hour = closing_hour
                min_penalty = total_penalty
        return best_hour