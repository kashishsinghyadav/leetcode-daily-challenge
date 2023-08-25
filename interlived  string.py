class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:



        def reach(i,j,k,s1,s2,s3,dp):

            if i<0 and j<0 and k<0:
                return True

            if i>=0 and j>=0 and dp[i][j]!=-1:
                return dp[i][j]
           
            

            
            if (i>=0 and s1[i]==s3[k] ) and (j>=0 and s2[j]==s3[k]):

                dp[i][j]= (reach(i-1,j,k-1,s1,s2,s3,dp) or reach(i,j-1,k-1,s1,s2,s3,dp))
                return dp[i][j]
                
            elif j>=0 and  s2[j]==s3[k]:
                dp[i][j]= reach(i,j-1,k-1,s1,s2,s3,dp)
                return dp[i][j]
            elif i>=0 and s1[i]==s3[k]:
                dp[i][j] = reach(i-1,j,k-1,s1,s2,s3,dp)
                return dp[i][j]


            else:
                dp[i][j]=False
                return dp[i][j]


        n=len(s1)
        m=len(s2)
        l=len(s3)
        dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]
        if l!=m+n:
            return False
        return reach(n-1,m-1,l-1,s1,s2,s3,dp)
