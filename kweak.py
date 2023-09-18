class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        lst=[]
        n=len(mat)
        m=len(mat[0])
        d={}
        ans=0
        for i in range(n):
            for j in range(m):
                ans+=mat[i][j]

            d[i]=ans
            lst.append(ans)
            ans=0
        print(lst)
        

        d=dict(sorted(d.items(),key = lambda x:x[1]))
        print(d)
        a=[]
        for key,val in d.items():
            if len(a)==k:
                break
            a.append(key)
        return a
