class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        for num in nums:
            if count[num]>1:
                z = num
        n= len(nums)
        actual_sum = n*(n+1)//2
        aarr_sum = sum(nums)-z
        miss = actual_sum-aarr_sum

        return [z,miss]
        