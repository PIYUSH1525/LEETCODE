class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        squares = [x * x for x in nums]
        squares.sort()
        return sum(squares[n//2:]) - sum(squares[:n//2])
        