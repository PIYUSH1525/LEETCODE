class Solution:
    def countCollisions(self, directions: str) -> int:
        trimmed_left = directions.lstrip("L")
        trimmed_both = trimmed_left.rstrip("R")
        total_cars_in_middle = len(trimmed_both)
        stationary_cars = trimmed_both.count("S")
        collisions = total_cars_in_middle - stationary_cars
      
        return collisions
