class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        z = set(nums)
        longest = 0
        for num in z:
            if num-1 not in z:
                current = num
                streak =1
                while current +1 in z:
                    current+=1
                    streak+=1
                longest = max(longest,streak)
        return longest