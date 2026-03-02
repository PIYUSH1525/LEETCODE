class Solution:
  def minSwaps(self, grid: list[list[int]]) -> int:
    n = len(grid)
    ans = 0
    suffixZeros = [n if 1 not in row else row[::-1].index(1) for row in grid]

    for i in range(n):
      neededZeros = n - 1 - i
      j = next((j for j in range(i, n) if suffixZeros[j] >= neededZeros), -1)
      if j == -1:
        return -1
      for k in range(j, i, -1):
        suffixZeros[k] = suffixZeros[k - 1]
      ans += j - i

    return ans