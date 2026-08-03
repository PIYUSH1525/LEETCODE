class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        from functools import cache
        from math import inf
        @cache
        def dfs(index: int) -> int:
            if index >= n:
                return 0
            max_score_diff = -inf
            current_sum = 0
          
            for num_stones in range(3):
                if index + num_stones >= n:
                    break
                current_sum += stoneValue[index + num_stones]
                score_diff = current_sum - dfs(index + num_stones + 1)
                max_score_diff = max(max_score_diff, score_diff)
          
            return max_score_diff
      
        n = len(stoneValue)
      
        alice_score_diff = dfs(0)
      
        if alice_score_diff == 0:
            return 'Tie'
        elif alice_score_diff > 0:
            return 'Alice'
        else:
            return 'Bob'
