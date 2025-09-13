class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a','e','i','o','u'}
        freq = Counter(s)
        vowel_freq= 0
        consonent_freq= 0
        for char, count in freq.items():
            if char in vowels:
                vowel_freq = max(vowel_freq,count)
            else:
                consonent_freq = max(consonent_freq, count)
        return vowel_freq + consonent_freq