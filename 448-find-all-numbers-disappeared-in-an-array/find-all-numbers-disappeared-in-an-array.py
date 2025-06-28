class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for number in nums:
            index = abs(number) - 1
            if nums[index] > 0:
                nums[index] *= -1
        missing_numbers = [i + 1 for i, x in enumerate(nums) if x > 0]
      
        return missing_numbers
        