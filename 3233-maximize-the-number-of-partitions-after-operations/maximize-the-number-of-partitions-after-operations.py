class Solution:
  def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
    @functools.lru_cache(None)
    def dp(i: int, canChange: bool, mask: int) -> int:
      if i == len(s):
        return 0

      def getRes(newBit: int, nextCanChange: bool) -> int:
        newMask = mask | newBit
        if newMask.bit_count() > k:
          return 1 + dp(i + 1, nextCanChange, newBit)
        return dp(i + 1, nextCanChange, newMask)

      res = getRes(1 << (ord(s[i]) - ord('a')), canChange)

      if canChange:
        for j in range(26):
          res = max(res, getRes(1 << j, False))
      return res

    return dp(0, True, 0) + 1