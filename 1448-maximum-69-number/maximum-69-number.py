class Solution:
    def maximum69Number(self, num: int) -> int:
        z =  str(num)
        return int(z.replace('6','9',1))
        # res = []
        # while num > 0:
        #     res.append(num % 10)
        #     num = num // 10
        # res = res[::-1]
        # print(res)
        # for i in range(len(res)):
        #     if res[i] != 9 :
        #         res[i] = 9
        #         break
        # string_numbers = map(str, res)
        # z = "".join(string_numbers)
        # return int(z)