class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        n=len(t)
        l=0
        if len(s)==0:
            return True
        for i in range(n):
            if t[i]==s[l]:
                l+=1
            if l==len(s):
                return True
        if l==len(s):
            return True
        return False
