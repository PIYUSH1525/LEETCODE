class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0.0
        for point1 in points:
            x1, y1 = point1
            for point2 in points:
                x2, y2 = point2       
                for point3 in points:
                    x3, y3 = point3
                    vector1_x = x2 - x1
                    vector1_y = y2 - y1
                    vector2_x = x3 - x1
                    vector2_y = y3 - y1
                    cross_product = vector1_x * vector2_y - vector2_x * vector1_y
                    area = abs(cross_product) / 2.0
                    max_area = max(max_area, area)
      
        return max_area