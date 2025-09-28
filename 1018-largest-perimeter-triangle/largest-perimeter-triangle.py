class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            largest_side = nums[i]
            middle_side = nums[i - 1]
            smallest_side = nums[i - 2]

            if smallest_side + middle_side > largest_side:
                return smallest_side + middle_side + largest_side
        return 0