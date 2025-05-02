class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s= Counter(magazine)
        for c in ransomNote:
            s[c] -= 1
            if s[c] < 0:
                return False
        return True 

        