class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def is_sorted(idx, modifier):
            for i in range(n):
                if A[idx + i] != A[idx] + i*modifier: 
                    return False
            return True

        n, A = len(nums), nums + nums
        first, last = A.index(0), A.index(n - 1)

        if is_sorted(first, 1):
            return min(first, n - 1 - last + 2)

        if is_sorted(last, -1):
            return min(last + 1, n - 1 - first + 1)

        return -1