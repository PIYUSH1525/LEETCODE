class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
      
        for num in nums:
            if num == 2:
                result.append(-1)
            else:
                for bit_position in range(1, 32):
                    if ((num >> bit_position) & 1) ^ 1:
                        result.append(num ^ (1 << (bit_position - 1)))
                        break
      
        return result