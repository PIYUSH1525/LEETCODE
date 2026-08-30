class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        mi = min(nums)
        mx = max(nums)

        i = nums.index(mi)
        j = nums.index(mx)

        a = min(i, j)
        b = max(i, j)

        left = b + 1
        right = n - a
        both = (a + 1) + (n - b)

        return min(left, right, both)