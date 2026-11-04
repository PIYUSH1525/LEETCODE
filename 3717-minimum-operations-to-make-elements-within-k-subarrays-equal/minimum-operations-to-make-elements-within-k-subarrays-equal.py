class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        from sortedcontainers import SortedList

        mid = (x-1)//2
        sl = SortedList(nums[:x])
        left_part_sum = sum(sl[:mid+1])
        right_part_sum = sum(sl[mid+1:])
        
        costs = [float('inf') for _ in range(len(nums))]
        costs[x-1] = (x - x//2) * sl[mid] - left_part_sum + right_part_sum - x//2 * sl[mid]
            
        for i in range(x, len(nums)):
            added = nums[i]
            outed = nums[i-x]

            outed_idx = sl.bisect_left(outed)
            if outed_idx <= mid:
                left_part_sum -= outed
                left_part_sum += sl[mid+1]
                right_part_sum -= sl[mid+1]
            else:
                right_part_sum -= outed
            sl.remove(outed)
            
            added_idx = sl.bisect_left(added)
            if added_idx <= mid:
                left_part_sum += added
                left_part_sum -= sl[mid]
                right_part_sum += sl[mid]
            else:
                right_part_sum += added
            sl.add(added)
            
            cost = (x - x//2) * sl[mid] - left_part_sum + right_part_sum - x//2 * sl[mid]
            costs[i] = cost
        
        dp = [float('inf') for _ in range(len(nums))]
        for i in range(x-1, len(nums)):
            dp[i] = min(dp[i-1], costs[i])
        for i in range(1, k):
            new_dp = [float('inf') for _ in range(len(nums))]
            for j in range(x*(i+1)-1, len(nums)):
                new_dp[j] = min(new_dp[j-1], costs[j] + dp[j-x])
            dp = new_dp

        return dp[-1]