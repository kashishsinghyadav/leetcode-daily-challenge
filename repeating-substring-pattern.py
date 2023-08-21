class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        new=(s+s)[1:-1]
        return s in new
        
