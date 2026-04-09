class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        limit = math.isqrt(n)
        lightK = defaultdict(list)
        
        for q in queries:
            l, r, k, v = q
            
            if k >= limit:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            else:
                lightK[k].append(q)
                
        for k, query_list in lightK.items():
            diff = [1] * n
            
            for q in query_list:
                l, r, _, v = q
                diff[l] = (diff[l] * v) % MOD
                steps = (r - l) // k
                nxt = l + (steps + 1) * k
                if nxt < n:
                    diff[nxt] = (diff[nxt] * pow(v, -1, MOD)) % MOD
            for i in range(n):
                if i >= k:
                    diff[i] = (diff[i] * diff[i - k]) % MOD
                nums[i] = (nums[i] * diff[i]) % MOD
                
        ans = 0
        for num in nums:
            ans ^= num
            
        return ans