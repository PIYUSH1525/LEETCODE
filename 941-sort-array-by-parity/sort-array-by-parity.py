class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_place = 0

        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[even_place], nums[i] = nums[i], nums[even_place]
                even_place += 1
        return nums
        # l = 0 
        # r = 1
        # while r < len(nums):
        #     if nums[l] % 2 != 0 :
        #         if nums[r] %2 == 0:
        #             nums[l] , nums[r] = nums[r] , nums[l]
        #             l+=1
        #         r+=1
        #     else:
        #         l+=1
        #         if l ==r:
        #             r+=1       
        # return  nums 