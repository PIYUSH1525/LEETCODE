class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = Counter(nums)
        # nums: freq
        for x in hashMap:
            if hashMap[x] ==1:
                return x