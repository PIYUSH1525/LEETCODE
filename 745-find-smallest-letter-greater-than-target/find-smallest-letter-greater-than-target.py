class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)-1
        result = letters[0]
        while l <=r:
            mid  = (l+r)//2
            if letters[mid] > target:
                result = letters[mid]
                r = mid-1 
            else:
                l = mid+1
             
        return result