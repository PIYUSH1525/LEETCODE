class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}
        for i in range(len(nums)):
            if (target - nums[i]) in c:
                return [c[target - nums[i]],i]
            else:
                c[nums[i]] = i
        
        return []
        