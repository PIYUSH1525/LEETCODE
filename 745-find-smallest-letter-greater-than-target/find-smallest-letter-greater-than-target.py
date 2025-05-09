class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) 
        while l < r:
            mid = (l+r)//2
            if ord(letters[mid]) > ord(target):
                r = mid
            else:
                l = mid + 1
        return letters[l % len(letters)]
       