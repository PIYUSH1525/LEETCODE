class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        first_true_index = -1
        while left <= right:
            mid = (left + right) 
            if nums[mid] <= nums[n - 1]:
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1
        return nums[first_true_index]