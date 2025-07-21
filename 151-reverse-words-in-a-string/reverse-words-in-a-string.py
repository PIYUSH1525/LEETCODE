class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        a.reverse()

        return ' '.join(a)
        