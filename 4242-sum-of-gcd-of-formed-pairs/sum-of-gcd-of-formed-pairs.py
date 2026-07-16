class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixgcd = []
        curr_max = 0
        for num in nums:
            curr_max = max(curr_max,num)
            prefixgcd.append(math.gcd(num,curr_max))

        prefixgcd.sort()

        total = 0
        n = len(prefixgcd)
        for i in range(n//2):
            total+=math.gcd(prefixgcd[i],prefixgcd[n-1-i])
        return total