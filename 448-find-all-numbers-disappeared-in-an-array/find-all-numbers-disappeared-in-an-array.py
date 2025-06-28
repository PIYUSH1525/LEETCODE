class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # count = Counter(nums)
        counter = set(nums)

        count = 1

        result = []

        while count <= len(nums):

            if count not in counter:

                result.append(count)

            count += 1    
        return result
        # return [i for i in range(1, len(nums)+1) if i not in count]

        