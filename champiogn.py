class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        def pour(poured,i,j,dp):
            if i<0 or j<0 or i<j:
                return 0.0
            if i==0 and j==0:
                return poured
            if dp[i][j]!=-1:
                return dp[i][j]

            left= (pour(poured,i-1,j-1,dp)-1)/2.0
            right=(pour(poured,i-1,j,dp)-1)/2.0
            if left<0:
                left= 0.0
            if right<0:
                right= 0.0
            dp[i][j]=left+right
            return dp[i][j]

        dp=[[-1 for _ in range(101)] for _ in range(101)]
        return min(1.0,pour(poured,query_row,query_glass,dp))
        
