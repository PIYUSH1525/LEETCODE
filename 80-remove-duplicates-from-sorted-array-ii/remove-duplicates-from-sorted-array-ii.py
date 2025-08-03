class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        r =2
        for i in range(2,len(nums)):
            if nums[i] !=nums[r-2]:
                nums[r] = nums[i]
                r+=1 
        return r