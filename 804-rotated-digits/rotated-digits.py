nums = []
for n in range(1, 10**4+1):
    s = str(n)
    if ("2" in s or "5" in s or "6" in s or "9" in s) and ("3" not in s and "4" not in s and "7" not in s):
        nums.append(n)

class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        return bisect.bisect(nums, n) 