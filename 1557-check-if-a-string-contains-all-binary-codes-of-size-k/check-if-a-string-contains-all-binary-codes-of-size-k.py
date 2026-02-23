class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        string_length = len(s)
        total_possible_codes = 1 << k
        if string_length - k + 1 < total_possible_codes:
            return False
        unique_substrings = {s[i:i + k] for i in range(string_length - k + 1)}
        return len(unique_substrings) == total_possible_codes