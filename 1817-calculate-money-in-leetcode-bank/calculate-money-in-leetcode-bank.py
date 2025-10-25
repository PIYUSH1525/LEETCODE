class Solution:
    def totalMoney(self, n: int) -> int:
        complete_weeks, remaining_days = divmod(n, 7)
        first_week_sum = 28
        last_week_sum = 28 + 7 * (complete_weeks - 1)
        total_from_complete_weeks = (first_week_sum + last_week_sum) * complete_weeks // 2
        first_day_amount = complete_weeks + 1
        last_day_amount = complete_weeks + remaining_days
        total_from_remaining_days = (first_day_amount + last_day_amount) * remaining_days // 2
      
        return total_from_complete_weeks + total_from_remaining_days