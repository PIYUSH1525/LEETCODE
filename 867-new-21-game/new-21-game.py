class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        P = [0.0] * (n + 1)
        P[0] = 1.0
        currProbabSum = 1.0 if k > 0 else 0.0
        for i in range(1, n + 1):
            P[i] = currProbabSum / maxPts
            if i < k:
                currProbabSum += P[i]
            if i - maxPts >= 0 and i - maxPts < k:
                currProbabSum -= P[i - maxPts]
        return sum(P[k:])