class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ''
        substrings = []
        balance = 0
        start = 0
        for i in range(len(s)):
            balance += 1 if s[i] == '1' else -1
            if balance == 0:
                inner_content = self.makeLargestSpecial(s[start + 1:i])
                special_substring = '1' + inner_content + '0'
                substrings.append(special_substring)
                start = i + 1
        substrings.sort(reverse=True)
        return ''.join(substrings)