class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0  # Pointer for non-zero elements
        r = 1  # Pointer for searching non-zero elements

        while r < len(nums):  # Iterate through the list
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]  # Swap zero with non-zero
                l += 1  # Move l to next position
            elif nums[l] != 0:
                l += 1  # Move l if it's already a non-zero number
            r += 1  # Always move r forward
        
        return nums
            
            
        