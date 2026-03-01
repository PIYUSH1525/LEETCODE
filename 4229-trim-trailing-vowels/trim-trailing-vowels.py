class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        lis = list(s)
        n = len(lis)
        arr = ['a', 'e', 'i', 'o','u']
        for i in range(n-1,-1,-1):
            if lis[i] in arr:
                lis.pop(i)
            else:
                break
        return "".join(lis)
