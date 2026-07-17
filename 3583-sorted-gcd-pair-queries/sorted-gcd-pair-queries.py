from typing import List
from collections import Counter
from itertools import accumulate
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_value = max(nums)
        frequency_count = Counter(nums)
        gcd_pair_count = [0] * (max_value + 1)
        for gcd in range(max_value, 0, -1):
            multiples_count = 0
            for multiple in range(gcd, max_value + 1, gcd):
                multiples_count += frequency_count[multiple]
                gcd_pair_count[gcd] -= gcd_pair_count[multiple]
            gcd_pair_count[gcd] += multiples_count * (multiples_count - 1) / 2

        # Create prefix sum array for binary search
        prefix_sum = list(accumulate(gcd_pair_count))

        # For each query, find the GCD value using binary search on prefix sum
        return [bisect_right(prefix_sum, query) for query in queries]