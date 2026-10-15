class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            counts = {}
            d = 0
            for j in range(i, n):
                x = nums[j]
                if counts.get(x, 0) == 0:
                    d += 1
                counts[x] = counts.get(x, 0) + 1
                ans += d**2
        return ans