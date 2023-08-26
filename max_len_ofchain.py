class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n=len(pairs)
        dp=[0 for i in range(n)]
        dp[n-1]=1
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if pairs[i][1]<pairs[j][0]:
                    dp[i]=max(dp[i],1+dp[j])
        
        return max(dp)
