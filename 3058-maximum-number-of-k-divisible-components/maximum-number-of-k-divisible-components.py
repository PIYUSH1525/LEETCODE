class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        def dfs(node: int, parent: int) -> int:
            subtree_sum = values[node]
            for neighbor in adjacency_list[node]:
                if neighbor != parent:
                    subtree_sum += dfs(neighbor, node)
            if subtree_sum % k == 0:
                nonlocal component_count
                component_count += 1
          
            return subtree_sum
        adjacency_list = [[] for _ in range(n)]
        for node_a, node_b in edges:
            adjacency_list[node_a].append(node_b)
            adjacency_list[node_b].append(node_a)
      
        component_count = 0
      
        dfs(0, -1)
      
        return component_count