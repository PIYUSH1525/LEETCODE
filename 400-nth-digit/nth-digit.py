class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1       
        count = 9       
        start = 1        

        # Step 1: Find the range in which the nth digit falls
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        # Step 2: Find the actual number that contains the nth digit
        number = start + (n - 1) // length

        # Step 3: Find the digit within that number
        digit_index = (n - 1) % length
        return int(str(number)[digit_index])
        