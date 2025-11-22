class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        j = 0
        k = n
        while k < len(nums):
            res.append(nums[j])
            res.append(nums[k])
            j+=1
            k+=1
        return res
                 
