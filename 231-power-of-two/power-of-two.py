class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #Soulution 2
        return ( n & n-1) == 0 and n > 0
        
    
        #SOLUTION 1
        # if n <=0 :
        #     return False
        # while n >=0:
        #     if n%2==0:
        #         n=n/2
        #     else:
        #         break
        # if n==1:
        #     return True
        # else:
        #     return False