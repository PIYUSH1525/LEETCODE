class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for f in counter.values():
            if f > 2:
                return False
        return True
        