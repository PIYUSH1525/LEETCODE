class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_chars_match = sorted(s1[::2]) == sorted(s2[::2])
        odd_chars_match = sorted(s1[1::2]) == sorted(s2[1::2])
        return even_chars_match and odd_chars_match