class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                word_list = list(word)
                l, r = 0, i
                while l < r:
                    word_list[l], word_list[r] = word_list[r], word_list[l]
                    l += 1
                    r -= 1
                return ''.join(word_list)
        return word 


        
        