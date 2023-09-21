class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a=[]
        n=len(s)
        for i in range(n):
            if s[i]==c:
                a.append(i)

        j=0
        ans=[]
        for i in range(n):
            if  s[i]==c:
                ans.append(0)
                j+=1
            elif i<a[0]:
                ans.append(a[0]-i)
            elif i>a[-1]:
                ans.append(i-a[-1])
            else:
                ans.append(min((i-a[j-1]),(a[j]-i)))
        return ans
