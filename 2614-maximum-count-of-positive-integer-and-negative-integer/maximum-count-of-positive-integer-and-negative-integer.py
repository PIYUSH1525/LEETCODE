class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def find_first_zero():
            l = 0 
            r= len(nums)
            while l<r:
                mid = (l+r) //2
                if nums[mid] < 0:
                    l = mid+1
                else :
                    r = mid
            return l 
        def find_first_pos():
            l = 0 
            r= len(nums)
            while l<r:
                mid = (l+r) //2
                if nums[mid] <= 0:
                    l = mid+1
                else :
                    r = mid
            return l 
        neg_count = find_first_zero()
        pos_count = len(nums) - find_first_pos()
        return max(neg_count, pos_count)

        # pos = 0
        # neg = 0
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         pos+=1
        #     elif nums[i]< 0:
        #         neg+=1
        # return max(pos,neg)