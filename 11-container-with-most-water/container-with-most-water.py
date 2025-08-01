class Solution:
    def maxArea(self, height: List[int]) -> int:
        l =0
        r= len(height)-1
        maxx = 0
        while l<r:
            if height[l]<height[r]:
                water= min(height[l],height[r])* (r-l)
                maxx = max(maxx, water)
                l+=1
            else:
                water= min(height[l],height[r])* (r-l)
                maxx = max(maxx, water)
                r-=1
        return maxx
        # l = 0 
        # r = len(height)-1
        # max_water = 0
        # while l < r:
        #     current_area = (r - l) * min(height[l], height[r])
        #     max_water = max(max_water, current_area)
        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return max_water



        