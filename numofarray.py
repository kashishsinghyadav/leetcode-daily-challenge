class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod=10**9+7


        def solve(idx,cost,maxi,dp):
            if idx==n:
                if cost==k:
                    return 1
                else:
                    return 0
            if dp[idx][cost][maxi]!=-1:
                return dp[idx][cost][maxi]
            

            res=0
            for i in range(1,m+1):
                if i>maxi:
                    res+= solve(idx+1,cost+1,i,dp)
                else:
                    res+= solve(idx+1,cost,maxi,dp)

            dp[idx][cost][maxi]= res%mod
            return dp[idx][cost][maxi]

        dp=[[[-1 for _ in range(100+1)]for _ in range(51)] for _ in range(51)]
        return solve(0,0,0,dp)

        
