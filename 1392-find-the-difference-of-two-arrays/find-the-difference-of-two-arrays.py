class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 = []
        res2= []
        for num in nums1:
            if num not in nums2:
                if num not in res1:
                    res1.append(num)
        for numm in nums2:
            if numm not in nums1:
                if numm not in res2:
                    res2.append(numm)
        return [res1,res2]
        