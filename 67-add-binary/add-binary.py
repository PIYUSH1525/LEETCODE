class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i= len(a)-1
        j =len(b)-1
        carry =0
        res = []
        while i>=0 or j >=0 or carry>0:
            dig_a = a[i] if i>=0 else 0
            dig_b = b[j] if j>=0 else 0
            summ = int(dig_a)+ int(dig_b)+ carry
            res.append(str(summ%2))
            carry = summ//2
            i-=1
            j-=1
        return "".join(res[::-1])