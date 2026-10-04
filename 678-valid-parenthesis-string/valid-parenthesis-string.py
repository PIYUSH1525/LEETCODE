class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        star = []
        for idx, char in enumerate(s):
            if char == '(':
                stk.append( idx )
            elif char == ')':
                if stk:
                    stk.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append( idx )
        while stk and star:
            if stk[-1] > star[-1]:
                return False
            stk.pop()
            star.pop()
        return len(stk) == 0
                