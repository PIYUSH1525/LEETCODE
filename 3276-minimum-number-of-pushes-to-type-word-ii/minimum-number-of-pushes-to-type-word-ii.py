from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        char_frequency = Counter(word)
        total_pushes = 0
        sorted_frequencies = sorted(char_frequency.values(), reverse=True)
        for index, frequency in enumerate(sorted_frequencies):
            pushes_per_char = (index // 8) + 1
            total_pushes += pushes_per_char * frequency
        return total_pushes
