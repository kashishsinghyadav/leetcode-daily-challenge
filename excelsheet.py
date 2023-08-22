class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s=''
        while(columnNumber>0):
            columnNumber-=1
            new=columnNumber%26
            s+=chr(65+new)
            columnNumber=columnNumber//26
        return s[::-1]
