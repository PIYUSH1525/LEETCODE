class Solution:
    def maxNumOfSubstrings(self, st: str) -> List[str]:
        letters = {}
        n = len(st)
        for i,a in enumerate(st):
            if a not in letters:
                letters[a] = [i,None]
        for i in range(n-1,-1,-1):
            a = st[i]
            if letters[a][1] is None:
                letters[a][1] = i
        
        for i,a in enumerate(st):
            for k in letters:
                if k==a:continue
                if letters[k][0]<i<letters[k][1]:
                    letters[k][0] = min(letters[k][0],letters[a][0])
                    letters[k][1] = max(letters[k][1],letters[a][1])
        keys = list(letters.keys())
        keys.sort(key = lambda x:letters[x])
        validints = []
        M = len(keys)
        seen = set([])
        res = []
        validints = list(letters.values())
        validints.sort(key = lambda x:x[1]-x[0])
        for s,e in validints:
            possible = True
            for ps,pe in res:
                if not (s > pe or e < ps):
                    possible = False
                    break
            if possible:
                res.append([s,e])
        return [st[a:b+1] for a,b in res]