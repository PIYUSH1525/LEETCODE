class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0
        summ = sum(nums[:k])
        MaxSum = summ
        l =0
        r = k
        while r< len(nums):
            summ -= nums[l]
            l+=1
            summ+= nums[r]
            r+=1
            MaxSum = max(summ,MaxSum)
        return MaxSum/k

            