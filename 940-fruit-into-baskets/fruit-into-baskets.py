class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        maxx = 0
        hashmap= defaultdict(int)
        for r in range(len(fruits)):
            hashmap[fruits[r]]+=1
            if len(hashmap)>2:
                hashmap[fruits[l]]-=1
                if hashmap[fruits[l]] ==0:
                    del hashmap[fruits[l]]
                l+=1
            maxx = max(maxx, r - l + 1)
        return maxx


