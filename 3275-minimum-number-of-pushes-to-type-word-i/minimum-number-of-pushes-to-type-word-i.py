class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        for i in range(len(word)):
            pushes += (i // 8) + 1
        return pushes