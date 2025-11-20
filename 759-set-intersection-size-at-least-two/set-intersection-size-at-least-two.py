class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[1], -interval[0]))
        second_last = -1
        last = -1
        result_size = 0
      
        for start, end in intervals:
            if start <= second_last:
                continue
            if start > last:
                result_size += 2
                second_last = end - 1
                last = end
            else:
                result_size += 1
                second_last = last
                last = end
      
        return result_size