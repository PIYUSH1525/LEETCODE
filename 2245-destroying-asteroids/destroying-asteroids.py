class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        count = 0
        n= len(asteroids)
        for i in range(n):
            if mass >= asteroids[i]:
                mass+=asteroids[i]
                count+=1
        if count == n:
            return True
        else:
            return False
        