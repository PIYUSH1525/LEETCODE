class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total_count = 0 
        consecutive_ones = 0  
        for char in s:
            if char == "1":
                consecutive_ones += 1
                total_count += consecutive_ones
            else:
                consecutive_ones = 0
        return total_count % MOD
