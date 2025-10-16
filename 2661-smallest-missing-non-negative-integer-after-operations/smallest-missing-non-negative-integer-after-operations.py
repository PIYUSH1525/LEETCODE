class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainder_count = Counter(num % value for num in nums)
    
        for i in range(len(nums) + 1):
            if remainder_count[i % value] == 0:
                return i
          
            remainder_count[i % value] -= 1