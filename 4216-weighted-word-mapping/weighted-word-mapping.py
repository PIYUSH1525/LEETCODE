class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        for word in words:
            total_weight = 0
            for char in word:
                index = ord(char) - ord('a')
                total_weight += weights[index]
            
            remainder = total_weight % 26
            mapped_char = chr(ord('z') - remainder)
            result.append(mapped_char)
            
        return "".join(result)