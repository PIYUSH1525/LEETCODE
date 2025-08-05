class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count_zero = 0
        count_one =0
        l,r=0,0
        res =0
        while r <len(s): 
            if s[r] =='0':
                count_zero+=1
            else:
                count_one+=1
            while count_zero>k and count_one>k:
                if s[l] =='0':
                    count_zero-=1
                else:
                    count_one-=1
                l+=1
            res += (r - l) + 1
            r+=1
        return res
           
        