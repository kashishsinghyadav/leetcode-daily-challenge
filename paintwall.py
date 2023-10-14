class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        
        n=len(cost)
        def  paint(idx,remain,dp):
            if remain<=0:
                return 0
            if idx>=n:
                return 1e9

            if dp[idx][remain]!=-1:
                return dp[idx][remain]

            take=cost[idx]+paint(idx+1,remain-1-time[idx],dp)
            nontake=0+paint(idx+1,remain,dp)

            dp[idx][remain]=min(take,nontake)
            return dp[idx][remain]

        dp=[[-1 for _ in range(501)] for _ in  range(501)]
       
        return paint(0,n,dp)
        
