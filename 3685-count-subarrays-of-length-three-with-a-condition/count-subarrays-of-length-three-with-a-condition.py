class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l = 0 
        r = 2
        count = 0
        while r< len(nums):
            mid = (l+r)//2
            midd = nums[mid]/2
            if nums[l] + nums[r]  == midd :
                count +=1
            l+=1
            r+=1
        return count 
