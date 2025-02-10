class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0  
        r = 1 
        while r < len(nums):  
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l] 
                l += 1  
            elif nums[l] != 0:
                l += 1 
            r += 1
        # n = len(nums)
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.append(nums[i])                    
        #         nums.remove(nums[i])
            
            
        