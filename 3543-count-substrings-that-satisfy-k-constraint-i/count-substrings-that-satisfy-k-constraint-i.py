class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count_zero = 0
        count_one = 0
        l,r = 0,0
        res =0
        while r <len(s):
            if s[r] == "0":
                count_zero+=1
            if s[r] =="1":
                count_one+=1
            while count_zero>k and count_one>k :
                if s[l] =="0":
                    count_zero-=1
                if s[l] =="1":
                    count_one-=1
                l+=1  
            curr = (r-l)+1
            res += curr  
            r+=1
            
        return res
