from bisect import bisect_right
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        cnt = [0] * (max_val + 1)
        for num in nums:
            cnt[num] += 1
            
        gcd_cnt = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            total_multiples = 0
            for j in range(i, max_val + 1, i):
                total_multiples += cnt[j]
            
            pairs = total_multiples * (total_multiples - 1) // 2
            
            for j in range(2 * i, max_val + 1, i):
                pairs -= gcd_cnt[j]
                
            gcd_cnt[i] = pairs
            
        pref = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            pref[i] = pref[i - 1] + gcd_cnt[i]
            
        ans = []
        for q in queries:
            idx = bisect_right(pref, q)
            ans.append(idx)
            
        return ans
        