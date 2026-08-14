class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        char_count = [0] * 26
        for end in range(len(s)):
            char_count[ord(s[end]) - ord('a')] += 1

            while char_count[ord(s[end]) - ord('a')] > 2:
                char_count[ord(s[start]) - ord('a')] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length