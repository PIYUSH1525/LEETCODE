class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        whole_sum =sum(nums)
        curr_sum = 0
        n  = len(nums)
        for i in range(n):
            if curr_sum == whole_sum - curr_sum - nums[i]:
                return i
            curr_sum += nums[i]
        return -1