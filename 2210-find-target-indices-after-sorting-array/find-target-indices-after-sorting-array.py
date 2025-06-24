class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        # brute force using loop O(n)
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res