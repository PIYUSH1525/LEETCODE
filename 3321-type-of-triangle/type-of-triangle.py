class Solution:
    def triangleType(self, nums: List[int]) -> str:
        s1 = nums[0]
        s2 = nums[1]
        s3 = nums[2]

        if s1 + s2 > s3 and  s2 + s3 > s1 and s1 + s3 > s2:
            if s1 == s2 ==s3:
                return "equilateral"
            elif s1 == s2 or s1==s3 or s2 ==s3:
                return "isosceles"
            elif s1!=s2!=s3:
                return "scalene"
        else :
            return "none"

        