class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for i in range(0, len(s), k):
            chunk = s[i : i + k]
            filled_chunk = chunk.ljust(k, fill)
            result.append(filled_chunk)
        return result
