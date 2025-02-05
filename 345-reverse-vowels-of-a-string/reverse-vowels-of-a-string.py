class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'aeiouAEIOU'
        x = list(s)
        l = 0
        r = len(x)-1
        while l < r:
            while l < r and x[l] not in vowel:
                l+=1
            while l < r and x[r] not in vowel :
                r-=1
            x[l] , x[r] = x[r] ,x[l]
            l+=1
            r-=1
        return "".join(x)

        

        