class Solution:
    def minDeletions(self, s: str) -> int:
        if len(s)==1:
            return 0
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] +=1
            else:
                d[s[i]]=1
       
        sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
        print(sorted_d)
        ans=set()
        fre=0
        for key,val in sorted_d.items():
            while val in ans:
                val-=1
                fre+=1
            if val>0:
                ans.add(val)
        return fre
