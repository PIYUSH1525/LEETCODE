class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        const long long MOD = 1000000007LL;
        unordered_map<int,int>cnt;
        cnt.reserve(points.size()*2);
        for(auto& p: points){
            ++cnt[p[1]];
        }
        vector<long long>v;
        v.reserve(cnt.size());

        for(auto& kv : cnt){
            long long c = kv.second;
            if(c>=2){
                v.push_back(c*(c-1)/2);
            }
        }
        if(v.size()<2) return 0;
        long long sum = 0, sumSq = 0;
        for(long long x:v){
            long long xm = x % MOD;
            sum = (sum+xm) % MOD;
            sumSq = (sumSq + xm * xm % MOD)% MOD;
        }
        long long res =((sum* sum % MOD - sumSq)%MOD + MOD)% MOD;
        long long inv2 = (MOD+1)/2;
        res = res*inv2 % MOD;
        return static_cast<int>(res);
    }
};