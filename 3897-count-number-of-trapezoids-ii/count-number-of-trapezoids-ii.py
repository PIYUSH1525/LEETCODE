from typing import List
from collections import defaultdict
import math

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
        slope_groups = defaultdict(lambda: defaultdict(int))
        midpoints = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                dy = y1 - y2
                dx = x1 - x2
                g = math.gcd(dy, dx)
                dy //= g
                dx //= g
                
                if dx < 0:
                    dy, dx = -dy, -dx
                elif dx == 0 and dy < 0:
                    dy = -dy
                
                slope = (dy, dx)
                
                line_id = dx * y1 - dy * x1
                
                slope_groups[slope][line_id] += 1
                
                mid_key = (x1 + x2, y1 + y2)
                midpoints[mid_key][slope] += 1

        total_trapezoids = 0
        for slope, lines in slope_groups.items():
            if len(lines) < 2:
                continue
            
            counts = list(lines.values())
            
            sum_counts = sum(counts)
            sum_sq_counts = sum(c * c for c in counts)
            
            total_trapezoids += (sum_counts * sum_counts - sum_sq_counts) // 2
            
        for mid, slopes in midpoints.items():
            if len(slopes) < 2:
                continue
            total_segments = sum(slopes.values())
            total_pairs = total_segments * (total_segments - 1) // 2
            same_slope_pairs = 0
            for count in slopes.values():
                same_slope_pairs += count * (count - 1) // 2
                
            parallelograms = total_pairs - same_slope_pairs
            total_trapezoids -= parallelograms
            
        return total_trapezoids