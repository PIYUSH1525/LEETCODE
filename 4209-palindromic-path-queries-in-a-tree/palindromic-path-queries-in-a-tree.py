class Solution:
    def palindromePath(self, n: int, E: list[list[int]], s: str, Q: list[str]) -> list[bool]:
        P, D = [0] * n, [0] * n
        D[0] = 2
        for u, v in E: P[u], P[v], D[u], D[v] = P[u] ^ v, P[v] ^ u, D[u] + 1, D[v] + 1

        SS, C, QQ = [1] * n, [-1] * n, [i for i in range(n) if D[i] == 1]
        for i in QQ:
            p, ss = P[i], SS[i]
            SS[p] += ss
            if (c := C[p]) == -1 or ss > SS[c]: C[p] = i

            P[p], D[p] = P[p] ^ i, D[p] - 1
            if D[p] == 1: QQ.append(p)
        QQ.append(0)

        T, D, L, t = [-1] * n, [-1] * n, [0] * n, 0
        for i in reversed(QQ):
            if ~D[i]: continue

            tt = i
            while ~i: T[i], L[t], D[i], t, i = tt, 1 << ord(s[i]) - 97, t, t + 1, C[i]
        
        B = [0] + L
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j <= n: B[j] ^= B[i]
        
        A = []
        for q in Q:
            match q.split():
                case ("update", i, c):
                    x = D[int(i)]
                    v = (1 << ord(c) - 97)
                    d = v ^ L[x]
                    L[x] = v
                    x += 1
                    while x <= n: B[x], x = B[x] ^ d, x + (x & -x)
                case ("query", u, v):
                    u, v = map(int, (u, v))
                    r = 0
                    while T[u] != T[v]:
                        if D[T[u]] < D[T[v]]: u, v = v, u
                        ss, tt = D[T[u]], D[u] + 1
                        while tt > ss: r, tt = r ^ B[tt], tt & (tt - 1)
                        while ss > tt: r, ss = r ^ B[ss], ss & (ss - 1)
                        u = P[T[u]]
                    if D[u] > D[v]: u, v = v, u
                    ss, tt = D[u], D[v] + 1
                    while tt > ss: r, tt = r ^ B[tt], tt & (tt - 1)
                    while ss > tt: r, ss = r ^ B[ss], ss & (ss - 1)
                    A.append(r & (r - 1) == 0)
        return A