class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        for num in range(left, right + 1):
            set_bits_count = num.bit_count()
            if set_bits_count in prime_numbers:
                count += 1
              
        return count