class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def back(f=1,cur=[]):
            if len(cur)==k:
                ans.append(cur[:])
                return 
            for i in range(f,n+1):
                cur.append(i)
                back(i+1,cur)
                cur.pop()
        ans=[]
        back()
        return ans
