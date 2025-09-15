class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = [False] * 26
        for ch in brokenLetters:
            broken[ord(ch) - ord('a')] = True

        result = 0
        foundBroken = False
        for ch in text:
            if ch == ' ':  
                if not foundBroken:
                    result += 1
                foundBroken = False  
            elif broken[ord(ch) - ord('a')]:
                foundBroken = True 
        if not foundBroken:
            result += 1

        return result