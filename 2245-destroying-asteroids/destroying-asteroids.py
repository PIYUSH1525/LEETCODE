class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        max_ast = max(asteroids)
        
        counts = [0] * (max_ast + 1)
        for ast in asteroids:
            counts[ast] += 1
            
        current_mass = mass
        
        for ast_mass in range(1, max_ast + 1):
            if counts[ast_mass] > 0:
                if current_mass < ast_mass:
                    return False
                
                current_mass += ast_mass * counts[ast_mass]
                
        return True