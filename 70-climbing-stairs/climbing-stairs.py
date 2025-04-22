class Solution:
    def climbStairs(self, n: int) -> int:
        prev_step, curr_step = 0, 1
        for _ in range(n):
            prev_step, curr_step = curr_step, prev_step + curr_step
        return curr_step