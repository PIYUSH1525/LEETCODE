class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n =  len(nums)
        if n < 3 :
            return -1
        nums.sort()
        product = max(nums[n-3]*nums[n-2]*nums[n-1],nums[0]*nums[1]*nums[n-1])
        return product

        
        