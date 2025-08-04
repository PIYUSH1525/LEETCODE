class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        l,r = 0,k
        max_avg = summ/k
        while r < len(nums):
            summ+=nums[r]
            summ-=nums[l]
            l+=1
            r+=1
            curr = summ/k
            max_avg = max(max_avg,curr)
        return max_avg

        