from typing import List
from math import inf
class Solution:
    def minimumCost(
        self,source: str,target: str,original: List[str],changed: List[str],cost: List[int],) -> int:
        graph = [[inf] * 26 for _ in range(26)]
        for i in range(26):
            graph[i][i] = 0
        for orig_char, changed_char, transform_cost in zip(original, changed, cost):
            from_index = ord(orig_char) - ord('a')
            to_index = ord(changed_char) - ord('a')
            graph[from_index][to_index] = min(graph[from_index][to_index], transform_cost)
        for intermediate in range(26):
            for start in range(26):
                for end in range(26):
                    graph[start][end] = min(
                        graph[start][end], 
                        graph[start][intermediate] + graph[intermediate][end]
                    )
        total_cost = 0
        for source_char, target_char in zip(source, target):
            if source_char != target_char:
                from_index = ord(source_char) - ord('a')
                to_index = ord(target_char) - ord('a')
                if graph[from_index][to_index] >= inf:
                    return -1
              
                total_cost += graph[from_index][to_index]
      
        return total_cost
