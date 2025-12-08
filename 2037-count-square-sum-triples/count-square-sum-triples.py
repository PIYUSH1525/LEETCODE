import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n):
            for b in range(1, n):
                sum_of_squares = a * a + b * b
                c = int(math.sqrt(sum_of_squares))
                if c <= n and c * c == sum_of_squares:
                    count += 1                  
        return count
