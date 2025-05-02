class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num //2
        if num ==1:
            return True    
        while l<=r:
            mid = (l+r) //2
            if mid *mid == num:
                return True
            elif mid*mid < num:
                l = mid+1
            elif mid*mid > num:
                r = mid-1
        return False
        