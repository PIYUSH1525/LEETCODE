class Solution:
    def getDivisors(self,n):
        divs=[]
        i=1
        while i*i<=n:
            if n%i==0:
                divs.append(i)
                if i!=n//i:
                    divs.append(n//i)
            i+=1
        return divs

    def check(self,nums,k):
        n=len(nums)
        last=-10**9

        for i in range(0,n,k):
            cnt=0
            mn=10**9
            mx=-10**9

            for j in range(i,i+k):
                mn=min(mn,nums[j])
                mx=max(mx,nums[j])
                nxt=nums[i] if j==i+k-1 else nums[j+1]
                if nums[j]>nxt:
                    cnt+=1

            if cnt>1 or last>mn:
                return False
            last=mx
        return True

    def sortableIntegers(self,nums):
        ans=0
        for k in self.getDivisors(len(nums)):
            if self.check(nums,k):
                ans+=k
        return ans