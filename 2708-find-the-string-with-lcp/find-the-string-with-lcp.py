from typing import List
from string import ascii_lowercase

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        result_string = [""] * n
        current_position = 0
        for character in ascii_lowercase:
            while current_position < n and result_string[current_position]:
                current_position += 1
            if current_position == n:
                break
            for j in range(current_position, n):
                if lcp[current_position][j] > 0:
                    result_string[j] = character
        if "" in result_string:
            return ""
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if result_string[i] == result_string[j]:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""
                else:
                    if lcp[i][j] != 0:
                        return ""
        return "".join(result_string)
