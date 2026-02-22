class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        player_1 = 0
        player_2 = 0
        player1_active = True
        n  = len(nums)
        for i in range(n):
            if nums[i]%2 != 0 :
                player1_active = not player1_active
            if i % 6 ==5:
                player1_active = not player1_active
            if player1_active:
                player_1 += nums[i]
            else:
                player_2 += nums[i]
        return player_1 - player_2