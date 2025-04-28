class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set([j for j in jewels]) 
        count = 0 
        for s in stones :
            if s in jewels :
                count+=1
        return count 
        
        
        # count = 0
        # for char in stones:
        #     if char in jewels:
        #         count+=1
        # return count

        
        