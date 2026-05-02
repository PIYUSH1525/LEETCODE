class Solution:
    def rotatedDigits(self, n: int) -> int:
      
        def is_good_number(number):
            rotated_number = 0
            temp_number = number
            place_value = 1
          
            while temp_number:
                digit = temp_number % 10
                if rotation_map[digit] == -1:
                    return False
                rotated_number = rotation_map[digit] * place_value + rotated_number
                place_value *= 10
                temp_number //= 10
            return number != rotated_number
        rotation_map = [0, 1, 5, -1, -1, 2, 9, -1, 8, 6]
        return sum(is_good_number(i) for i in range(1, n + 1))