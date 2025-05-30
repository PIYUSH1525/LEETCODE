class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)
        while l<r:
            m = (l+r)//2
            if (arr[m] - m - 1 >= k):
                r = m
            else:
                l = m + 1
        return l + k
