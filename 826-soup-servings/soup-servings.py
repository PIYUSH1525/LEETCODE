class Solution:
    def soupServings(self, n: int) -> float:
        if n>=4800:
                return 1.0
        nemo = {}
        serves= [(100,0),(75,25),(50,50),(25,75)]
        def solve(a,b):
            if (a,b) in nemo:
                return nemo[(a,b)]
            if a<=0 and b<=0:
                return 0.5
            if a <=0:
                return 1.0
            if b <= 0:
                return 0.0
            probablity = 0.0

            for serve_a , serve_b in serves:
                probablity += 0.25 * solve(a-serve_a , b-serve_b)
            nemo[(a,b)] = probablity
            return probablity
        return solve(n,n)
        