class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        total_ones = 0  
        index = 0
      
        previous_zero_segment = float('-inf') 
        max_zero_gain = 0  
      
        while index < n:
            segment_end = index + 1
            while segment_end < n and s[segment_end] == s[index]:
                segment_end += 1
          
            current_segment_length = segment_end - index
          
            if s[index] == '1':
                total_ones += current_segment_length
            else:
                max_zero_gain = max(max_zero_gain, 
                                   previous_zero_segment + current_segment_length)
                previous_zero_segment = current_segment_length
          
            index = segment_end
      
        result = total_ones + max_zero_gain
        return result