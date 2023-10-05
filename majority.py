class solutions:

def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for i in range(n):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1

        ans=[]
        for i,j in d.items():
            if j> math.floor(n/3):
                ans.append(i)
        return ans
