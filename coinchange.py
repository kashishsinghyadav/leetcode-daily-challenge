class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        def count(amount , coins ,n,dp):
            if n==0:
                if amount%coins[0] == 0:
                    return 1
                else:
                    return 0

            if dp[n][amount] != -1:
                return dp[n][amount]

            pick = count(amount,coins,n-1,dp)
            notpick = 0
            if coins[n]<=amount:
                notpick=count(amount-coins[n],coins,n,dp)

            dp[n][amount]=pick + notpick
            return dp[n][amount]


        n=len(coins)
        dp=[[-1 for _ in range(amount+1)] for _ in range(n)]
        return count(amount,coins,n-1,dp)
