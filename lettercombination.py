class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        res=[]
        if digits=="":
            return 
        def bfs(pos:int,st:str):
            if pos == len(digits):res.append(st)
            else:
                letter = d[digits[pos]]
                for i in letter:
                    
                    bfs(pos+1,st+i)
        bfs(0,"")
        return res
                
