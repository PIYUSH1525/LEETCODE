class Solution:
  def maximumScore(self, grid: list[list[int]]) -> int:
    n = len(grid)
    prefix = [[0] * (n + 1) for _ in range(n)]
    prevPick = [0] * (n + 1)
    prevSkip = [0] * (n + 1)

    for j in range(n):
      for i in range(n):
        prefix[j][i + 1] = prefix[j][i] + grid[i][j]

    for j in range(1, n):
      currPick = [0] * (n + 1)
      currSkip = [0] * (n + 1)
      for curr in range(n + 1):  
        for prev in range(n + 1):  
          if curr > prev:
            score = prefix[j - 1][curr] - prefix[j - 1][prev]
            currPick[curr] = max(currPick[curr], prevSkip[prev] + score)
            currSkip[curr] = max(currSkip[curr], prevSkip[prev] + score)
          else:
            score = prefix[j][prev] - prefix[j][curr]
            currPick[curr] = max(currPick[curr], prevPick[prev] + score)
            currSkip[curr] = max(currSkip[curr], prevPick[prev])
      prevPick = currPick
      prevSkip = currSkip

    return max(prevPick)