class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n >0:
            if n%4 ==0:
                n = n/4
            else:
                break
        return True if n ==1 else False