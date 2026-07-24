class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        st = set()
        for x in nums:
            for y in nums:
                st.add(x ^ y)

        ans = set()
        for x in st:
            for y in nums:
                ans.add(x ^ y)

        return len(ans)