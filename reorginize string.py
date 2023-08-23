from heapq import heappush,heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:return ""
        heap=[]
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        for key,value in d.items():
            heapq.heappush(heap,[-value,key])

        res=""
        pre=heapq.heappop(heap)
        res+=pre[1]
        while heap:
            curr = heapq.heappop(heap)
            res+=curr[1]


            pre[0]+=1
            if pre[0]<0:
                heapq.heappush(heap,pre)
            pre=curr
        return "" if len(res)!=len(s) else res
                
            



