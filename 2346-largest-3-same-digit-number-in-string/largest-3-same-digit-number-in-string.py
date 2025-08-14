class Solution:
    def largestGoodInteger(self, num: str) -> str:
        prev = "A"
        count =  0
        res = []
        if len(num) <3:
            return ""
        for i in range(len(num)):
            if num[i] == prev:
                count+=1
            else:
                prev = num[i]
                count=1
            if count == 3:
                res.append(num[i])
        if len(res) ==0:
            return ""
        z = max(res),max(res),max(res)
        return("".join(z))