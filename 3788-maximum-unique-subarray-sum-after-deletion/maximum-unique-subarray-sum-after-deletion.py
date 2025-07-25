class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = []
        res2 = []
        for i in nums:
            if i >= 0:
                res.append(i)
            else:
                res2.append(i)
        x =set(res)
        if max(nums) <0:
            return max(nums)
        else:
            return sum(x)
        