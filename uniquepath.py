class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:



        def num_ways(i,j,dp):
            if i>=0 and j>=0 and obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0


            if dp[i][j]!=-1:
                return dp[i][j]

            left_ways=num_ways(i-1,j,dp)
            right_ways=num_ways(i,j-1,dp)

            dp[i][j]=left_ways+right_ways
            return dp[i][j]
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        
        dp=[[-1 for _ in range(m)] for _ in range(n)]
        return num_ways(n-1,m-1,dp)
