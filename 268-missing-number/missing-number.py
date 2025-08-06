class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]!= 0:
            return 0
        l,r =0,1

        while r< len(nums):
            if nums[r]!= nums[l]+1:
                return nums[r]-1
            r+=1
            l+=1
        return max(nums)+1
                

    
        