from sortedcontainers import SortedList
    
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        sl = SortedList()
        n = min(5 * 10 ** 4, len(queries) * 3)
        sl.add(0)
        sl.add(n)
        
        ans = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                sl.add(x)
        gap = SortedList()
        gap.add((0, 0))
        curr = 0
        for x, y in pairwise(sl):
            if (g := y - x) > curr:
                gap.add((y, g))
                curr = g
        
        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]
                index = sl.index(x)
                after = sl[index + 1]
                before = sl[index - 1]
                sl.remove(x)
                g = after - before
                index = gap.bisect_left((x, 0))
                while index < len(gap) and gap[index][1] <= g:
                    gap.pop(index)
                if gap[index - 1][1] < g:
                    gap.add((after, g))
            else:
                _, x, sz = q
                index = sl.bisect_right(x)
                before = sl[index - 1]
                index = gap.bisect_right((before, math.inf)) - 1
                ans.append((x - before) >= sz or gap[index][1] >= sz)
            
        ans.reverse()
        return ans