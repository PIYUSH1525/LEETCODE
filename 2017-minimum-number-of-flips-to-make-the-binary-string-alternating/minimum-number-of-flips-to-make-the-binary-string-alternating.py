class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        target_pattern = "01"
        mismatch_count = sum(char != target_pattern[i & 1] for i, char in enumerate(s))
        min_flips = min(mismatch_count, n - mismatch_count)
        for i in range(n):
            mismatch_count -= s[i] != target_pattern[i & 1]
            mismatch_count += s[i] != target_pattern[(i + n) & 1]
            min_flips = min(min_flips, mismatch_count, n - mismatch_count)
      
        return min_flips