class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x_position = 0
        y_position = 0
        for move in moves:
            if move == "U":  
                y_position += 1
            elif move == "D":  
                y_position -= 1
            elif move == "L":  
                x_position -= 1
            elif move == "R":  
                x_position += 1
        return x_position == 0 and y_position == 0