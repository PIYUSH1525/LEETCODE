class Solution:
    def sortVowels(self, s: str) -> str:
        v1 = ("aeiou")
        v2 = ("AEIOU")
        final = []
        for char in s:
            if char in v1 or char in v2:
                final.append(char)
        final.sort()
        l = 0
        s_list = list(s)
        for i in range(len(s)):
            if s_list[i] in v1 or s_list[i] in v2:
                s_list[i] = final[l]
                l+=1
        return "".join(s_list)