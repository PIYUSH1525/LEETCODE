class Solution:
    def numberOfPairs(self, points):
        points.sort(key=lambda point: (point[0], -point[1]))
        answer = 0  
        for i, (_, y1) in enumerate(points):
            max_y = -inf 
            for _, y2 in points[i + 1:]:
                if max_y < y2 <= y1:
                    max_y = y2  
                    answer += 1 
        return answer 
