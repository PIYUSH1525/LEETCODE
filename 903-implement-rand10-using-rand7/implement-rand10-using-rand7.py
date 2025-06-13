# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num = (rand7() - 1) * 7 + rand7()  # Gives 1 to 49
            if num <= 40:
                return num % 10 + 1
        