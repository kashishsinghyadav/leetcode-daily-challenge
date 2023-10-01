class Solution:
    def reverseWords(self, s: str) -> str:
        new_str=s.split()
        st1=[]
        for i in new_str:
            st1.append(i[::-1])
        k=' '.join(map(str,st1))
        return k
    
        
        
