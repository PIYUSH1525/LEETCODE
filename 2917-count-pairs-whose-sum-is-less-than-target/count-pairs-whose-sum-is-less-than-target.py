class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # count = 0
        # for i in range (len(nums)):
        #     for j in range (i+1,len(nums)):
        #         if   nums[i]+ nums[j] < target :
        #             count+=1
        # return count
        low=0
        nums.sort()
        high=len(nums)-1
        pair=0
        while(low<high):
            if(nums[low]+nums[high]<target):
                pair+=high-low
                low+=1
            else:
                high-=1
        return pair

        