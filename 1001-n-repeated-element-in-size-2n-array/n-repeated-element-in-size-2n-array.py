class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen_elements = set()
        for num in nums:
            if num in seen_elements:
                return num
            seen_elements.add(num)