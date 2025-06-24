class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        # brute force using loop O(n)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         res.append(i)
        # return res
        # using Counting
        less = equal = 0
        for num in nums:
            if num < target:
                less += 1
            elif num == target:
                equal += 1
        return list(range(less, less + equal))