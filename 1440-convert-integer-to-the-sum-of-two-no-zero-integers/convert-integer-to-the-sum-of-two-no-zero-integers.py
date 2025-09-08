class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            b = n- i
            if "0" not in str(i) and "0" not in str(b):
                return [i,b]