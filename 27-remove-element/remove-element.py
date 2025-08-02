class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r= len(nums)-1
        while l <=r:
            if nums[r] == val:
                r-=1
                continue 
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r-=1
            l+=1
        return l

                
            