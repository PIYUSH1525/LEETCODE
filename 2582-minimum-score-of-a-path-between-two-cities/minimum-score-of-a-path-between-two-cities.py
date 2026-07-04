from collections import defaultdict
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for node_a, node_b, distance in roads:
            graph[node_a].append((node_b, distance))
            graph[node_b].append((node_a, distance))
        visited = [False] * (n + 1)  
        min_score = float('inf')
      
        def depth_first_search(current_node):
            nonlocal min_score
            for neighbor, edge_weight in graph[current_node]:
                min_score = min(min_score, edge_weight)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    depth_first_search(neighbor)
        visited[1] = True
        depth_first_search(1)
      
        return min_score