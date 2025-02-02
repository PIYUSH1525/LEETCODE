class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = []
        for i in range(1,n+1):
            if n % i == 0:
                factor.append(i)
        if k > len(factor):
            return -1
        else:
            return factor[k-1]
        