class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(filter(str.isalnum, s)).lower()
        return new == new[::-1]