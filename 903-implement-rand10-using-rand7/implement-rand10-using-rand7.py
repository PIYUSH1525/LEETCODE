# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7() - 1
            col = rand7()
            value = row * 7 + col
            if value <= 40:
                return value % 10 + 1
        