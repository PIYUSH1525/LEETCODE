class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == key and abs(i - j) <= k:
                    result.append(i)
                    break  # No need to check more j's for this i

        return result