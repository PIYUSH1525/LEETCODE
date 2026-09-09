class Solution:
    def countCommas(self, n: int) -> int:
        start = 1000

        commas = 1

        answer = 0

        while start <= n:
            if start > n // 1000:
                end = n
            else:
                end = start * 1000 - 1

            count = end - start + 1

            answer += count * commas

            start *= 1000

            commas += 1

        return answer