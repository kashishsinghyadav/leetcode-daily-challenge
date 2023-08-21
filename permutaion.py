class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def per(s,j,ans,nums):
            if s==j:
                ans.append(nums[:])

            else:
                for i in range(s,j+1):
                    nums[i],nums[s]=nums[s],nums[i]
                    per(s+1,j,ans,nums)
                    nums[i],nums[s]=nums[s],nums[i]

            
        ans=[]
        per(0,len(nums)-1,ans,nums)
        return ans
