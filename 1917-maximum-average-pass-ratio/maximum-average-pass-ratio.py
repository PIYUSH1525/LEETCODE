import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        pq = []
        for p, t in classes:
            gain = (p + 1) / (t + 1) - p / t
            heapq.heappush(pq, (-gain, p, t))
        for _ in range(extraStudents):
            neg_gain, p, t = heapq.heappop(pq)
            p += 1
            t += 1
            new_gain = (p + 1) / (t + 1) - p / t
            heapq.heappush(pq, (-new_gain, p, t))
        total_pass_ratio = 0
        for neg_gain, p, t in pq:
            total_pass_ratio += p / t
            
        return total_pass_ratio / len(classes)