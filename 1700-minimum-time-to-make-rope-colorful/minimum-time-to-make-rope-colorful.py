class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        min_time = 0
        left = 0 
        n = len(colors)
        for right in range(1, n):
            if colors[left] == colors[right]:
                if neededTime[left] < neededTime[right]:
                    min_time += neededTime[left]
                    left = right
                else:
                    min_time += neededTime[right]
            else:
                left = right
                
        return min_time