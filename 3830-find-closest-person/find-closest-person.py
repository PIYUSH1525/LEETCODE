class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a = abs(z -x) 
        b = abs(z -y)
        if a < b:
            return 1
        elif b<a:
            return 2
        else:
            return 0