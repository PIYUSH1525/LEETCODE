class Solution:
    def partitionString(self, s: str) -> int:
        hash1 = set()
        count = 1
        for i in s :
            if i in hash1:
                count+=1
                hash1.clear()
            hash1.add(i)
        

        return count
        