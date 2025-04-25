class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        v = "aeiouAEIOU"
        r = len(s)-1
        l = 0 
        while l < r:
            while (l<r and s[l] not in v):
                l+=1
            while (r>l and s[r] not in v):
                r-=1
            s[l], s[r] = s[r] , s[l]
            l+=1
            r-=1
        return "".join(s)
