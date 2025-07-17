
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        count_matrix = [[0] * k for _ in range(k)]
        max_length = 0
        for num in nums:
            rem = num % k
            for j in range(k):
                compl = (j - rem + k) % k
                count_matrix[rem][compl] = count_matrix[compl][rem] + 1
                max_length = max(max_length, count_matrix[rem][compl])
        return max_length