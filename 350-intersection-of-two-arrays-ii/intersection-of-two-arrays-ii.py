class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        element_counter = Counter(nums1)
        intersection_result = []
      
        for num in nums2:
            if element_counter[num] > 0:
                intersection_result.append(num)
                element_counter[num] -= 1
        return intersection_result