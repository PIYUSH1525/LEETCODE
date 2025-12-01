class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries)

        while left < right:
            mid = (left + right + 1) >> 1
            total_contribution = sum(min(battery_capacity, mid) for battery_capacity in batteries)

            if total_contribution >= n * mid:
                left = mid
            else:
                right = mid - 1

        return left