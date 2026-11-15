class Solution:
    def numOfSubarrays(self, a: List[int]) -> int:
        res = p = 0
        for i,v in enumerate(a):
            p = (p,i-p+1)[v&1]
            res += p
        return res%(10**9+7)