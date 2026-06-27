class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        s = Counter(nums)
        ans = 1

        if 1 in s:
            if s[1] % 2 == 0:
                ans = s[1] - 1
            else:
                ans = s[1]

        for x in s:
            if x == 1:
                continue

            curr = x
            length = 0

            while s[curr] >= 2:
                length += 2
                curr *= curr

            if s[curr] == 1:
                cand = length + 1
            else:
                cand = length - 1

            ans = max(ans, cand)

        return ans