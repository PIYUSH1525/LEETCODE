class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        maxx =0 
        for i in range(len(nums)):
            if nums[i] ==0:
                count+=1
                maxx+=count
            else:
                count=0
        return maxx