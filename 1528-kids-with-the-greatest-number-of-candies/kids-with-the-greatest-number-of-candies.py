class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        j = max(candies)
        for i in range (len(candies)):
            if candies[i] + extraCandies >= j:
                res.append(True)
            else:
                res.append(False)
        return res
        