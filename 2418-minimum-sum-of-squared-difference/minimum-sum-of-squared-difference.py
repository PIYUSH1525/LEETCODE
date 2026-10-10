class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        heap = [-abs(a - b) for a, b in zip(nums1, nums2)]
        su = -sum(heap)
        if su <= k1 + k2:
            return 0
        heapify(heap)
        delta = k1 + k2
        
        while delta > 0:
            diff = -heappop(heap)
            step = math.ceil(delta / len(nums2))
            diff -= step
            delta -= step
            heappush(heap, -diff)
        
        return sum(e ** 2 for e in heap)