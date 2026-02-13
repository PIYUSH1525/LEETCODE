class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for idx, num in enumerate(nums):
            diff = target-num
            if diff in seen:
                return  [seen[diff],idx]
            else:
                seen[num] = idx
        return -1