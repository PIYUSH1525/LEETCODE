class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        s1 = Counter(basket1)
        s2 = Counter(basket2)
        check = s1+s2
        res = 0
        for fruit,count in check.items():
            if count%2 !=0:
                return-1
        excess_count = s1-s2
        final = []
        excess_in_b1 = s1 - s2
        for fruit, count in excess_in_b1.items():
            final.extend([fruit] * (count // 2))
        excess_in_b2 = s2 - s1
        for fruit, count in excess_in_b2.items():
            final.extend([fruit] * (count // 2))
        final.sort()
        min_el = min(min(basket1), min(basket2))
        for i in range(len(final)//2):
            swap_cost =min(2*min_el,final[i])
            res+=swap_cost
        return res

            