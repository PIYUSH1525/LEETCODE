class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0
        idx = 0
        for i in range (len(nums))  :
            if nums[i] == 0:
                zero+=1
            if nums[i] == 1:
                one+=1
            if nums[i] == 2:
                two+=1
        for i in range(zero):
            nums[idx] = 0
            idx+=1
        for i in range(one):
            nums[idx] = 1
            idx+=1
        for i in range(two):
            nums[idx] = 2
            idx+=1
            