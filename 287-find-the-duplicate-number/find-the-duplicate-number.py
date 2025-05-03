class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = Counter(nums)
        for num in nums :
            if n[num] >1:
                return num
        