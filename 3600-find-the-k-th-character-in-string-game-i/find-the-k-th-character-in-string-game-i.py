class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = ['a']
        while len(ans) < k:
            temp = []
            for ch in ans:
                if ch == 'z':
                    temp.append('a')
                else:
                    temp.append(chr(ord(ch) + 1))
            ans += temp
        
        return ans[k - 1]
