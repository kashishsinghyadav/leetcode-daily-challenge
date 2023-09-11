class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d={}
        ans=[]
        for val,size in enumerate(groupSizes):
           
            if size not in d:
                
                d[size]=[]
            d[size].append(val)
            if len(d[size])==size:
                ans.append(d[size])
                d[size]=[]
        return ans
