class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        sett =set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                    a, b, c = digits[i], digits[j], digits[k]
                    if a == 0:
                        continue
                    if c%2 != 0:
                        continue
                    num = a * 100 + b * 10 + c
                    sett.add(num)
        return len(sett)

         