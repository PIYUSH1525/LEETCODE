class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        from functools import cache
      
        @cache
        def dfs(left: int, right: int) -> int:
            if left + 1 == right:
                return 0
            min_score = float('inf')
            for k in range(left + 1, right):
                current_score = (dfs(left, k) + 
                                dfs(k, right) + 
                                values[left] * values[k] * values[right])
                min_score = min(min_score, current_score)
            return min_score
        return dfs(0, len(values) - 1)
