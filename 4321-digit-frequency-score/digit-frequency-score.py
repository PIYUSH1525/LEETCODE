class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        score = 0
        j = str(n)
        c = Counter(j)

        for num, freq in c.items():
            curr = int(num)*freq
            score+=curr
        return score