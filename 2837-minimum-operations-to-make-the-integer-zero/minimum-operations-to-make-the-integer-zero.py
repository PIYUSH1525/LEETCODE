from itertools import count

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in count(1):
            tar = num1 - i * num2
            if tar < 0:
                break
            if tar.bit_count() <= i <= tar:
                return i
        return -1