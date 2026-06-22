from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count = Counter(text)
        char_count['o'] //= 2
        char_count['l'] //= 2
        return min(char_count[c] for c in 'balon')