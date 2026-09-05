class Solution:
    def firstStableIndex(self, nums, k):

        n = len(nums)

        Max = [0] * n
        Min = [0] * n

        Max[0] = nums[0]

        for i in range(1, n):
            Max[i] = max(nums[i], Max[i - 1])

        Min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            Min[i] = min(nums[i], Min[i + 1])

        for i in range(n):

            diff = Max[i] - Min[i]

            if diff <= k:
                return i

        return -1