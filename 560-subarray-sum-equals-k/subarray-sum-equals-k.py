class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        su = 0
        count = 0
        prefix_sums = defaultdict(int)
        for i in range(len(nums)):
            su+=nums[i]
            if su ==k :
                count+=1
            if (su - k) in prefix_sums:
                count += prefix_sums[su - k]
            prefix_sums[su] += 1
        return count
            
        