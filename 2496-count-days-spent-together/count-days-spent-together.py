class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)

        if end < start:
            return 0

        sm, sd = int(start[:2]), int(start[3:])
        em, ed = int(end[:2]), int(end[3:])

        d = sum(days[sm - 1:em])

        return d - (sd - 1) - (days[em - 1] - ed)