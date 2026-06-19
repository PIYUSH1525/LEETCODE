class Solution:
  def largestAltitude(self, gain: list[int]) -> int:
    

    res = 0
    curr = 0 
    for g in gain:
        curr+=g
        res = max(res,curr)
    return res