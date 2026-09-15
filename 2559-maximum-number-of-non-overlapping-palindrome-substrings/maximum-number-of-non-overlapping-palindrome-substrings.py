class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        last_end = count = 0

        for center in range(2 * n):
            left = center // 2
            right = left + center % 2

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= k:
                    end = right + 1

                    if left >= last_end:
                        last_end = end
                        count += 1
                    else:
                        last_end = min(last_end, end)

                    break

                left -= 1
                right += 1

        return count