class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split('.')
        b = version2.split('.')
        lenn = max(len(a), len(b))
        for i in range (lenn):
            val1 = int(a[i]) if i < len(a) else 0
            val2 = int(b[i]) if i < len(b) else 0


            if val1 < val2:
                return -1
            elif val1 > val2:
                return 1
        return 0