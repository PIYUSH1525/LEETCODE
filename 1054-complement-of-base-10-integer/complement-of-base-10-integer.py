class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a = bin(n)[2:]
        res = []
        for i in a :
            if i == '1':
                res.append('0')
            else:
                res.append('1')
        return int(''.join(res),2)