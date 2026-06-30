class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen_index = {"a": -1, "b": -1, "c": -1}
        total_count = 0
        for current_index, char in enumerate(s):
            last_seen_index[char] = current_index
          
            min_index = min(last_seen_index["a"], last_seen_index["b"], last_seen_index["c"])
          
            total_count += min_index + 1
      
        return total_count