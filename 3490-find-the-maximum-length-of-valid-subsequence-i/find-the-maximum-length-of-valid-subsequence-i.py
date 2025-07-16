class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        k = 2
        remainder_count = [[0] * k for _ in range(k)]
        max_length = 0
        for num in nums:
            remainder = num % k
            for j in range(k):
                previous_remainder = (j - remainder + k) % k
                remainder_count[remainder][previous_remainder] = remainder_count[previous_remainder][remainder] + 1
               
                max_length = max(max_length, remainder_count[remainder][previous_remainder])
      
        return max_length