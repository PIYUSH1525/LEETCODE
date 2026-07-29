class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        k -= 1
        import math
        def multinomial(_, lst):
            res, i = 1, sum(lst)
            i0 = lst.index(max(lst))
            for a in lst[:i0] + lst[i0+1:]:
                for j in range(1,a+1):
                    res *= i
                    res //= j
                    i -= 1
            return res
        basis = [i for i in s]
        
        basis.sort()
        
        cnt = defaultdict(int)
        for i in basis:
            cnt[i] += 1
            
        
        mid = ''
        
        for i in range(len(basis)):
            if cnt[basis[i]] % 2 == 1:
                mid = basis[i]
        
        back = []
        
        ans = []
        hit = False
        for i in basis:
            if cnt[i] == 1 and mid == i:
                continue
            if hit:
                cnt[i] -= 1
                hit = False
                continue
            cnt[i] -= 1
            ans.append(i)
            hit = True
        
        bas = []
        
        bottom = 0
        
        def yield_next(perm):
            from sortedcontainers import SortedSet
            
            if perm == sorted(perm)[::-1]:
                return [True, []]
            mini = 'a'
            
            midx = len(perm) - 1
            
            stacc = SortedSet()
            revback = defaultdict(int)
            for i in range(len(perm)-1, -1, -1):
                revback[perm[i]] = i
                if perm[i] < mini:
                    
                    
                    
                    thee = ''
                    
                    bottom = 0
                    top = len(stacc) - 1
                    while bottom < top:
                        middle = (bottom + top) >> 1
                        if stacc[middle] > perm[i]:
                            top = middle
                        else:
                            bottom = middle + 1
                    thee = stacc[bottom]
                            
                        
                    perm[i], perm[revback[thee]] = perm[revback[thee]], perm[i]
                    
                    hans = perm[:i + 1] + sorted(perm[i + 1:])
                    return [False, hans]
                if perm[i] > mini:
                    midx = i
                    mini = perm[i]
                stacc.add(perm[i])
            return [True, []]
        
        def qd(ans, kth):
            donk = []
        
            theses = ans[:]

            k = kth
            kth = k
            thee_idx = len(ans) - 1
            cntr = defaultdict(int)
            for i in range(len(ans)-1, -1, -1):

                donk.append(ans[i])

                cntr[ans[i]] += 1
                multi = []
                for intl in cntr.keys():
                    multi.append(cntr[intl])

                calc = multinomial(sum(multi), multi) - 1
                
                if calc <= k:

                    thee_idx = i
                    k = min(k, kth - calc)
                else:
                    break

                    
            ans = ans[:thee_idx] + sorted(ans[thee_idx:], reverse = True)
            return [ans, k]
            
        
        donk = []
        
        theses = ans[:]
        
        kth = k
        thee_index = len(ans) - 1
        cntr = defaultdict(int)
        for i in range(len(ans)-1, -1, -1):
            
            donk.append(ans[i])
            
            cntr[ans[i]] += 1
           
            multi = []
            for intl in cntr.keys():
                multi.append(cntr[intl])
                
            calc = multinomial(sum(multi), multi) - 1
            
            if calc <= k:
             
                thee_index = i
                k = min(k, kth - calc)
            else:
                break 
        ans = ans[:thee_index] + sorted(ans[thee_index:], reverse = True)
        
        yields = 10**8
        
        while k > 0:

            theta = yield_next(ans)
            if theta[0] == True:
                return ''
            ans = theta[1]
            k -= 1
            
            if k == 0:
                break
            pre = k
            if yields > 100:
                quickie = qd(ans, k)

                ans = quickie[0]
                k = quickie[1]
            post = k
            yields = pre - post
        return ''.join(ans) + mid + ''.join(ans[::-1])
                 
        
        