class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for ch in s:
            if ch == '*':
                if res:
                    res.pop()
            elif ch == '#':
                res.extend(res[:])
            elif ch == '%':
                res.reverse()
            else:
                res.append(ch)

        return ''.join(res)