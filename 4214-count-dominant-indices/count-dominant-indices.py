class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        count = 0 
        n = len(nums)
        for i in range(n-1):
            avg = sum(nums[i+1:])/len(nums[i+1:])
            if nums[i] > avg:
                count+=1
        return count