class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0
        for i in range(k):
            summ += nums[i]
        maxSum = summ
        l = 0 
        r = k
        while r < len(nums):
            summ -= nums[l]
            l+=1

            summ += nums[r]
            r+=1

            maxSum = max(maxSum ,summ)
        return maxSum/k