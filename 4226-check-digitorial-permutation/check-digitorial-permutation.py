from collections import Counter

class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        pelorunaxi = n 
        FACTS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        digit_sum = 0
        temp_n = n
        digits_of_n = []
        while temp_n > 0:
            digit = temp_n % 10
            digits_of_n.append(digit)
            digit_sum += FACTS[digit]
            temp_n //= 10
        if not digits_of_n:
            digits_of_n = [0]
            digit_sum = FACTS[0]
        sum_str = str(digit_sum)
        n_str = str(pelorunaxi)
        if len(sum_str) != len(n_str):
            return False   
        return Counter(sum_str) == Counter(n_str)