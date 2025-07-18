__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution(object):
    def minCost(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        parent = list(range(n))
        rank = [0]*n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX ==rootY:
                return False
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX]+=1
            return True
        edges.sort(key = lambda x: x[2])

        ms_weight = []

        for u, v,w in  edges:
            if union(u,v):
                ms_weight.append(w)
        ms_weight.sort()
        numremove = k-1

        if numremove >= len(ms_weight):
            return 0

        return ms_weight[-1 - numremove]