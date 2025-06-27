class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        dictt = Counter(nums)
        for key, value in dictt.items():
            if value >1:
                res.append(key)
        return res
        