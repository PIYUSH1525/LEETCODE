class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        result = ""
      
        for start in range(n):
            for end in range(start + k, n + 1):
                current_substring = s[start:end]
                if current_substring.count("1") == k:
                    if (not result or 
                        end - start < len(result) or 
                        (end - start == len(result) and current_substring < result)):
                        result = current_substring
      
        return result
