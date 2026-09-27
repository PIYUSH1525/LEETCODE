class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        ans = []
        while freq:
            for x in sorted(list(freq.keys())):
                ans.append(x)
                freq[x] -= 1
                if freq[x] == 0:
                    del freq[x]
        return ans
        