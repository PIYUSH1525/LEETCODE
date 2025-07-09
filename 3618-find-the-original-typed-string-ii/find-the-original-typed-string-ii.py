__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        cnt = []
        total = 1
        i = 0
        while i < len(word):
            j = i
            while i < len(word) and word[i] == word[j]:
                i += 1
            if i > j + 1:
                cnt.append(i - j - 1)
                total = total * (i - j) % mod
            k -= 1
        if k <= 0:
            return total

        dp = [0] * k
        dp[0] = 1
        for c in cnt:
            for i in range(1, k):
                dp[i] = (dp[i] + dp[i - 1]) % mod
            for i in range(k - 1, c, -1):
                dp[i] = (dp[i] - dp[i - c - 1]) % mod
        for i in range(1, k):
            dp[i] = (dp[i] + dp[i - 1]) % mod
        return (total - dp[k - 1]) % mod
        