class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        s1 = list(s)
        s2 = list(s)
        s1[:n-1] = sorted(s1[:n-1])
        s2[1:] = sorted(s2[1:])

        if list(s) == sorted(s):
            return 0

        if s1 == sorted(s1) or s2 == sorted(s2):
            return 1
        if s1[n-1] >= s1[0]:
            return 2
        if s2[0] <= s2[n-1]:
            return 2
        if n > 2:
            return 3

        return -1