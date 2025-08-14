class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = 0
        count = 0
        res =[]
        for r in range(len(num)):
            if num[l]!= num[r]:
                l=r
            if r - l + 1 == 3 and num[l] == num[r]:
                res.append(num[l])
        if not res:
            return ""
        max_digit = max(res)
        return max_digit * 3
        # prev = "A"
        # count =  0
        # res = []
        # if len(num) <3:
        #     return ""
        # for i in range(len(num)):
        #     if num[i] == prev:
        #         count+=1
        #     else:
        #         prev = num[i]
        #         count=1
        #     if count == 3:
        #         res.append(num[i])
        # if len(res) ==0:
        #     return ""
        # z = max(res),max(res),max(res)
        # return("".join(z))