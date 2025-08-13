import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    # #APPROCH2
    #     z = math.log(n, 3)
    #     if type(z) == int:
    #         return True
    #     else:
    #         return False



    #APPROACH 1
        if n <=0:
            return False
        while n >=0:
            if n%3 ==0:
                n = n/3
            else:
                break
        if n ==1:
            return True
        else:
            return False