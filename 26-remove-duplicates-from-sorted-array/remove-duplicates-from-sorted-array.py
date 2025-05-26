class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 
        r = 1
        while r < len(nums):
            if nums[l]!= nums[r]:
                l+=1
                nums[l] = nums[r]
            r+=1
        return l+1


        