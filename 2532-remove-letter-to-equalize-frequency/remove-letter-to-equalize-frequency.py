from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            temp_word = word[:i] + word[i+1:]
            freq_counts = Counter(temp_word)
            if len(set(freq_counts.values())) == 1:
                return True
        return False