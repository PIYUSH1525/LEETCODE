class Solution:
  def largestSubmatrix(self, matrix: list[list[int]]) -> int:
    ans = 0
    hist = [0] * len(matrix[0])
    for row in matrix:
      for i, num in enumerate(row):
        hist[i] = 0 if num == 0 else hist[i] + 1
      sortedHist = sorted(hist)
      for i, h in enumerate(sortedHist):
        ans = max(ans, h * (len(row) - i))

    return ans