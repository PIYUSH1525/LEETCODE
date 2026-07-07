class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n ==0:
            return 0
        x = 0
        res =[]
        for num in str(n):
            if num != "0":
                res.append(num)
                x += int(num)
        z = int("".join(res))
        return x*z