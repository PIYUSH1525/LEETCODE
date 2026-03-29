from collections import Counter

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        evens_match = Counter(s1[::2]) == Counter(s2[::2])
        odds_match = Counter(s1[1::2]) == Counter(s2[1::2])
        return evens_match and odds_match