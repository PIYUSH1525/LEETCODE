class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        s = Counter(nums)
        maxx = 0 
        res = 0

        for freq in s.values():
            if freq > maxx :
                maxx = freq
        for freq in s.values():
            if freq == maxx:
                res += freq        
        return res