class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                k -= 1
                if k == 0:
                    return i
        for i in reversed(factors):
            if i != n // i: 
                k -= 1
                if k == 0:
                    return n // i

        return -1

        
        
        # Approach 2
        # factor = []
        # for i in range(1,n+1):
        #     if n % i == 0:
        #         factor.append(i)
        # if k > len(factor):
        #     return -1
        # else:
        #     return factor[k-1]
        