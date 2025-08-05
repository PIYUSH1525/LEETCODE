class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits) 
        visited = [False] * n
        unplaced_count = n 
        for fruit in fruits:
            for index, basket in enumerate(baskets):
                if basket >= fruit and not visited[index]:
                    visited[index] = True  
                    unplaced_count -= 1 
                    break 
        return unplaced_count 