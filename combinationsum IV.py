class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        def comb(target,dp):
            if target==0:
                return 1
            if target<0:
                return 0

            if target in dp:
                return dp[target]

            dp[target]=0

            for i in nums:
                if i<=target:
                    dp[target]+=comb(target-i,dp)

            return dp[target]
        dp={}
        return comb(target,dp)
        
