class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        product_three_largest = nums[-1] * nums[-2] * nums[-3]
        product_two_smallest_one_largest = nums[-1] * nums[0] * nums[1]
        return max(product_three_largest, product_two_smallest_one_largest)