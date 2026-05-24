class Solution:
  def maxJumps(self, arr: list[int], d: int) -> int:
    n = len(arr)
    dp = [1] * n
    stack = []

    for i in range(n + 1):
      while stack and (i == n or arr[stack[-1]] < arr[i]):
        indices = [stack.pop()]
        while stack and arr[stack[-1]] == arr[indices[0]]:
          indices.append(stack.pop())
        for j in indices:
          if i < n and i - j <= d:
            dp[i] = max(dp[i], dp[j] + 1)
          if stack and j - stack[-1] <= d:
            dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)
      stack.append(i)

    return max(dp)