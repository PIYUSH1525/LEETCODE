class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) ==1:
            return intervals
        res= []
        intervals.sort()
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            last_end = res[-1][1]
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            if curr_start <= last_end:
                res[-1][1] = max(last_end, curr_end)     
            else:
                res.append(intervals[i])         
        return res  