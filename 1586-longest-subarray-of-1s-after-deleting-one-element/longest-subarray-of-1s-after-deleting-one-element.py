class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,r = 0 ,0
        z = 1
        lenn = 0
        while r< len(nums):
            if nums[r] ==0:
                z-=1
            if z<0:
                if nums[l] == 0:
                    z+=1   
                l+=1             
            curr = (r-l)+1
            lenn=  max(lenn , curr)
            r+=1
        return lenn-1

