class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        sett = set()
        n = len(nums)
        if n %2 != 0:
            return False
        for num in nums:
            if num in sett:
                sett.remove(num)
            else:
                sett.add(num)
        return len(sett) == 0
        
        


        