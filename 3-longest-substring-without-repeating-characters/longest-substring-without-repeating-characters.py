class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0
        max_length = 0
        for i in range (len(s)):
            while s[i] in sett:
                sett.remove(s[l])
                l+=1
            length =  (i-l)+1
            max_length = max(length , max_length)
            sett.add(s[i])
        return max_length
