class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in  nums:
            j = str(num)
            for i in j:
                res.append(int(i))
        return res