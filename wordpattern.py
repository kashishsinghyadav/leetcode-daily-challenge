class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split(" ")
        if len(pattern)!=len(word):return False
        h1={}
        h2={}

        for c,w in zip(pattern,word):
            if c in h1 and h1[c]!=w:
                return False
            if w in h2 and h2[w]!=c:
                return False

            h1[c]=w
            h2[w]=c
        return True
        
