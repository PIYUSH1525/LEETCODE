class Solution(object):
    def countCommas(self, n):
        if n < 1000:
            return 0

        return n - 999