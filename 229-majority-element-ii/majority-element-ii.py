class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        res = []
        n = (len(nums)//3)
        counter = Counter(nums)
        for num,count in counter.items():
            if count > n :
                res.append(num)
        return res

