class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        target = 1
        for v in arr:
            if v >= target:
                target += 1
        return target - 1