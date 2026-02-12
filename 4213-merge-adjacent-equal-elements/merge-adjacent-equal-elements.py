class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        res = []
        r,l = 0,1
        if len(nums) ==1:
            return nums
        else:
            res.append(nums[0])

        while l < len(nums):
            if nums[l] ==  res[r]:
                res[r] = res[r]+ nums[l]
                l+=1
            else:
                res.append(nums[l])
                l+=1
                r+=1
            while r> 0 and  res[r] == res[r-1]:
                res[r-1] = res[r-1]+res[r]
                res.pop(r)
                r-=1
        return res