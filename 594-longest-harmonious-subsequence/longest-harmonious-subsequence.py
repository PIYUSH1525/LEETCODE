class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        longe = 0
        for num in nums:
            if num + 1 in freq:
                current_length = freq[num] + freq[num + 1]
                longe = max(longe, current_length)
        return longe

        