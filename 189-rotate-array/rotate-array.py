class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        res = [0]*n
        for i in range(n):
            res[(i+k)%n] = nums[i]
        nums[:] =res 
        """
        Do not return anything, modify nums in-place instead.
        """
        