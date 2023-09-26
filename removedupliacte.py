class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n=len(s)
        d={}
        for i in range(n):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        print(d)
        stack=[]
        vis=set()
        for i in range(n):
            if s[i] in stack:
                d[s[i]]-=1
                continue

            while stack and ord(stack[-1])>ord(s[i]) and d[stack[-1]]>0:
                stack.pop()
                
            stack.append(s[i])
            
            d[s[i]]-=1
        print(stack)
        ans=""
        while stack:
            ans+=stack.pop()
        return ans[::-1]

            
        
