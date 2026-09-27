class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = []
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] = hashmap[num] + 1
        while hashmap:
            hashmap = dict(sorted(hashmap.items(), key=lambda v: v[0]))
            keys = []
            for key in hashmap:
                result.append(key)
                hashmap[key] = hashmap[key] - 1
                if hashmap[key] == 0:
                    keys.append(key)   
            for key in keys:
                if hashmap[key] == 0:
                    del hashmap[key]

        return result