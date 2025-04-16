class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l = len(word1)
        r = len(word2)
        n = min(l,r)
        for i in range(n):
            res += word1[i]+ word2[i]
        if l ==r:
            return res
        elif l< r:
            return res+ word2[n:]
        elif l>r:
            return res+ word1[n:]
        
        