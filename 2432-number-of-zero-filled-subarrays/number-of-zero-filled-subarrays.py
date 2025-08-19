class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res =0
        i=0
        while i < len(nums):
            if nums[i] ==0:
                l=0
                while i < len(nums) and nums[i] ==0 :
                    l+=1
                    i+=1
                res += (l*(l+1))//2
            else:
                i+=1          
        return res
        
            
        #APPROACH 1
        # count = 0
        # maxx =0 
        # for i in range(len(nums)):
        #     if nums[i] ==0:
        #         count+=1
        #         maxx+=count
        #     else:
        #         count=0
        # return maxx