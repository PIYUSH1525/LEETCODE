class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        arr = [("." + "#" * (n-1)) for i in range(m-1)]
        arr.append("."* n)
        return arr