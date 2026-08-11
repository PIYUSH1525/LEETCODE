class Solution:
    def missingInteger(self, A: List[int]) -> int:
        s, i = A[0], 1
        while i < len(A) and A[i - 1] + 1 == A[i]:
            s, i = s + A[i], i + 1
        B, res = set(A), s
        while res in B:
            res += 1
        return res