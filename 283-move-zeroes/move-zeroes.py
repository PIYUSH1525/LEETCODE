class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(nums[i])                    
                nums.remove(nums[i])
            
            
        