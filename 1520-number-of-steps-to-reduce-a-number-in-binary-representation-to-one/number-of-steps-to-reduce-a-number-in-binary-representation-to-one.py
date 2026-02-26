class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        num = int(s,2)
        while num > 1:
            if num%2==0:
                num = num//2
            else:
                num+=1
            count+=1
                
        return count 
        # carry = False 
        # steps = 0  
        # for bit in s[:0:-1]:
        #     if carry:
        #         if bit == '0':
        #             bit = '1' 
        #             carry = False  
        #         else:
        #             bit = '0' 
        #     if bit == '1':
        #         steps += 1  
        #         carry = True 
        #     steps += 1 
        # if carry:
        #     steps += 1
        # return steps