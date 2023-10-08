class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        m=len(nums2)
        dp=[[float('-inf') for _ in range(m)] for _ in range(n)]

        def maxpro(i,j):
            if i==n or j==m:
                return float('-inf')
            if dp[i][j]!=float('-inf'):
                return dp[i][j]

            dp[i][j] = max(nums1[i]*nums2[j]+max(maxpro(i+1,j+1),0),maxpro(i+1,j),maxpro(i,j+1))
            
            return dp[i][j]

        return maxpro(0,0)
