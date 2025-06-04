class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends==1 :
            return word
        res = ""
        longpossible = n - (numFriends - 1)
        for i in range(n):
            canTakeLength = min(longpossible, n - i)
            substr = word[i:i+canTakeLength]
            res = max(res, substr)

        return res
