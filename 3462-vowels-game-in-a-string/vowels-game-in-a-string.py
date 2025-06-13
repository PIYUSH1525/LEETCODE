class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for vow in 'aeiou':
            if vow in s:
                return True
        return False
        