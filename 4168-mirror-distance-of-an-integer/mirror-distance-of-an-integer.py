class Solution:
    def mirrorDistance(self, n: int) -> int:
        z = int(str(n)[::-1])
        return abs(n - z)