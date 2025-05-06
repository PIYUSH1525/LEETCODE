class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(nums[nums[i]])
        return res
        # n = len(nums)
        # for i in range(n):
        #     nums[i] = nums[i] + n * (nums[nums[i]]%n)

        # for i in range(n):
        #     nums[i] = nums[i]//n
        # return nums