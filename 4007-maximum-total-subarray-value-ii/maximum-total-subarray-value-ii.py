import heapq as hq
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = [(v, i) for i, v in enumerate(nums)]
        br = [n] * n 
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                br[i] = stack[-1]
            stack.append(i)

        sr = [n] * n 
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                sr[i] = stack[-1]
            stack.append(i)

        bl = [-1] * n 
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                bl[i] = stack[-1]
            stack.append(i)
        sl = [-1] * n 
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                sl[i] = stack[-1]
            stack.append(i)

        ns = sorted(nums)
        res = 0
        heap = [(ns[0][0] - ns[-1][0], ns[0], ns[-1], 0, n-1)]
        def ele(i, j):
            return (ns[i][0] - ns[j][0], ns[i], ns[j], i, j)
        def compose_next(i, j):
            res = []
            if i+1 <= j:
                res.append(ele(i+1, j))
            if i <= j-1:
                res.append(ele(i, j-1))
            return res
        visited = set([heap[0]])
        while k > 0:
            gap, mn, mx, nsl, nsr = hq.heappop(heap)
            for e in compose_next(nsl, nsr):
                if e not in visited:
                    hq.heappush(heap, e)
                    visited.add(e)
            mnv, mni = mn
            mxv, mxi = mx
            if mni <= mxi:
                if sr[mni] <= mxi or bl[mxi] >= mni:
                    continue
                lb = max(sl[mni] + 1, bl[mxi] + 1)
                rb = min(br[mxi] - 1, sr[mni] - 1)
                cnt = min((mni - lb + 1) * (rb - mxi + 1), k)
                res += cnt * abs(gap)
                k -= cnt
            else:
                if br[mxi] <= mni or sl[mni] >= mxi:
                    continue
                lb = max(bl[mxi] + 1, sl[mni] + 1)
                rb = min(sr[mni] - 1, br[mxi] - 1)
                cnt = min((mxi - lb + 1) * (rb - mni + 1), k)
                res += cnt * abs(gap)
                k -= cnt
            
        return res