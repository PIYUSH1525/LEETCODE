class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n= len(nums)
        l, r =0,n-1
        count = 0
        nums.sort()
        while l<r:
            if nums[l]+ nums[r] ==k:
                l+=1
                r-=1
                count+=1
            elif nums[l]+ nums[r] >k:
                r-=1
            elif nums[l]+ nums[r] <k:
                l+=1
        return count
