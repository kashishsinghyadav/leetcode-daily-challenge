class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        
        for i in s:
            if i.isalpha():
                length += 1
            else:
                length *= int(i)
        
        for i in reversed(s):
            k %= length
            if k == 0 and i.isalpha():
                return i
            if i.isalpha():
                length -= 1
            else:
                length //= int(i)
