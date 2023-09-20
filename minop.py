class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n=len(nums)
        total = sum(nums)-x

        if total==0:
            return n
        curr_sum=0
        max_len=0
        l=0

        for i,j in enumerate(nums):
            curr_sum+=j
            while l<=i and curr_sum>total:
                curr_sum -= nums[l]
                l += 1
            if curr_sum==total:
                max_len=max(max_len,i-l+1)
        return n - max_len if max_len else -1


        
