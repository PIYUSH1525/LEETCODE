class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s= -1
        e = -1
        for i in range (len(nums)):
            if nums[i] == target :
                if s == -1:
                    s = i
                e = i
        return [s,e]
                

            
        # l = 0
        # r = len(nums)-1
        # upp = 0
        # lower = 0
        # while l<= r:
        #     mid = (l+r)//2
        #     if nums[mid] == target:
        #         for i in range (mid, r):
        #             if nums[mid]== target:
        #                 upp = mid+1
                

        #     elif nums[mid] < target:
        #         l = mid+1
        #     elif nums[mid] > target:
        #         r = mid -1
        # return [-1,-1]
        