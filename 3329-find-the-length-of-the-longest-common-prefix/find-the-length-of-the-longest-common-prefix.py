class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_set = set()
        for num in arr1:
            while num > 0:
                prefix_set.add(num)
                num //= 10
        max_length = 0
        for num in arr2:
            while num > 0:
                if num in prefix_set:
                    max_length = max(max_length, len(str(num)))
                    break
                num //= 10
      
        return max_length