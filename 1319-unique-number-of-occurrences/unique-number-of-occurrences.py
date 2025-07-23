class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = list(Counter(arr).values())
        return len(freq) == len(set(freq))
        # has = dict(Counter(arr))
        # values = list(has.values())
        # values.sort()
        # if len(values) == 1:
        #     return True
        # for i in range(len(values)-1):
        #     if values[i] == values[i+1]:
        #         return False
        # return True