class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        digs=[]
        n=len(nums)
        for i in nums:
            cs=0
            cn=i
            while cn:
                cs+=cn%10
                cn//=10
            digs.append((cs,i))
        hm={}
        for i in range(n):
            hm[digs[i]]=i
        req=sorted(digs)
        res=0
        for i in range(n-1,-1,-1):
            cv=req[i]
            pos=hm.get(cv)
            av=digs[i]
            apos=hm.get(av)
            if pos!=apos:
                res+=1
                hm[av]=pos
                hm[cv]=apos
                digs[pos],digs[apos]=digs[apos],digs[pos]
        return res