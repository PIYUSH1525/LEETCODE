class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank = {}
        for i, num in enumerate(sorted_unique):
            rank[num] = i + 1
        result = []
        for num in arr:
            result.append(rank[num])
        
        return result
