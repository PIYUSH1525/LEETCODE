class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashmap = defaultdict(bool)
        for num in nums:
            if num >0 : # skip the Zero 
                hashmap[num] = True # esle 0 
        for i in range(1,len(nums)+2):
            if i not in hashmap:
                return i
        # for key,val in hashmap.items():
        #     if val <1:
        #         return key
        
        # return n+1

        

         