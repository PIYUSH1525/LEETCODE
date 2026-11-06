class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key = lambda x: x[1])
        s, e, count = 0, 0, 0
        ans, d = {}, defaultdict(int)
        for q in sorted(queries):
            while e < len(logs) and logs[e][1] <= q:
                d[logs[e][0]] += 1 
                if d[logs[e][0]] == 1:
                    count += 1 
                e += 1 
            while s < len(logs) and logs[s][1] < q-x:
                d[logs[s][0]] -= 1 
                if d[logs[s][0]] == 0:
                    count -= 1 
                s += 1 
            ans[q] = n-count
        return [ans[q] for q in queries]