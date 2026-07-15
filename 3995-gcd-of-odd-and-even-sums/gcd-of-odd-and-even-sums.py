class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(sumodd, sumeven):
            while sumeven != 0:
                sumodd, sumeven = sumeven, sumodd % sumeven
            return sumodd
        sumodd = 0
        sumeven = 0
        for i in range(1, n * 2 + 1):
            if i % 2 == 0:
                sumeven += i
            else:
                sumodd += i
        return gcd(sumodd, sumeven)