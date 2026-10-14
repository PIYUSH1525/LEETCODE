class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        s=""
        cSum=0
        d=9
        for i in range(num):
            if cSum+d>sum:
                while cSum+d>sum:
                    d-=1
                s+=str(d)
                cSum+=d
            else:
                if d==-1: break
                s+=str(d)
                cSum+=d
        return s if cSum==sum else ""