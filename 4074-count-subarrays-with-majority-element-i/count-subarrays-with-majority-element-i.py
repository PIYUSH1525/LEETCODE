class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            count = 0
            for j in range(i, n):
                if nums[j] == target:
                    count += 1

                if count > (j - i + 1) // 2:
                    ans += 1

        return ans
       
       
       
       ### TLE ### BRUTE FORCE ###
        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     for j in range(i,n):
        #         curr = 0
        #         for k  in range(i,j+1):
        #             if nums[k] == target:
        #                 curr+=1
        #         if curr> (j-i+1)//2:
        #             ans+=1
        # return ans