class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r =0,0
        size = 0
        while r < len(nums):
            if nums[r] ==0:
                k-=1
            if k<0:
                if nums[l]==0:
                    k+=1
                l+=1
            curr = (r-l)+1
            size = max(size ,curr)
            r+=1
        return size