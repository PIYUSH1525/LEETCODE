class Solution:
  def minBitwiseArray(self, nums: list[int]) -> list[int]:
    return [-1 if num == 2 else num - self._getLeadingOneOfLastGroupOfOnes(num)
            for num in nums]

  def _getLeadingOneOfLastGroupOfOnes(self, num: int) -> int:
    leadingOne = 1
    while (num & leadingOne) > 0:
      leadingOne <<= 1
    return leadingOne >> 1