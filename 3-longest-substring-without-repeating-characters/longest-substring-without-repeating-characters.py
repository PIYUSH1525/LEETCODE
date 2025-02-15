class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        max_count = 0
        l=0
        for i in range(len(s)):
            while s[i] in sett:
                sett.remove(s[l])
                l+=1
            
            length = (i-l) +1
            max_count = max(length, max_count)
            sett.add(s[i])
        return max_count
        
        