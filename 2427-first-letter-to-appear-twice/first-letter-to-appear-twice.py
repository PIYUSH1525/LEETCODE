class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ch = []
        for char in s :
            if char in ch:
                return char
            else:
                ch.append(char) 
        