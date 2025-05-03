class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        sum_nums = l*(l+1)/2
        sum_array = sum(nums) 
        
        return   int(sum_nums-sum_array  )