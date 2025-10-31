class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        total_operations = target[0]
        for i in range(1, len(target)):
            previous_height = target[i - 1]
            current_height = target[i]
            height_increase = max(0, current_height - previous_height)
            total_operations += height_increase
      
        return total_operations