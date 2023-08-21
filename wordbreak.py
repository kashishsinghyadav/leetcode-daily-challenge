class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        def word(n,s,i,dp):
            if i==n:
                return True


            if dp[i] is not None:
                return dp[i]
            

            for w in wordDict:
                if  i+len(w)<=len(s) and s[i:len(w)+i]==w:
                   
                    if word(n,s,len(w)+i,dp):
                        dp[i]=True
                        return True
            dp[i]=False
            return False
        n=len(s)
        dp=[None]*n
        return word(n,s,0,dp)  
