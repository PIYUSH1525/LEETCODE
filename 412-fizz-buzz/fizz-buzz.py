class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            res1 = (i%3 ==0)
            res2 = (i%5 ==0)
            if res1 and res2:
                res.append("FizzBuzz")
            elif res1:
                res.append("Fizz")
            elif res2:
                res.append("Buzz")
            else:
                res.append(str(i))
            
        return res