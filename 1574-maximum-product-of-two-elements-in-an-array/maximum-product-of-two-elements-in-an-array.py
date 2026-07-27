class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = 0
      
        for i, first_num in enumerate(nums):
            for second_num in nums[i + 1:]:
                current_product = (first_num - 1) * (second_num - 1)
                max_product = max(max_product, current_product)
      
        return max_product