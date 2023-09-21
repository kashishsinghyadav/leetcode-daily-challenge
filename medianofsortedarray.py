class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1 + nums2
        num.sort()
        print(num)
        n=len(num)
        if n%2==1:
            p=math.floor(n/2)
            
            return num[p]
        else:
            p=math.floor(n/2)
            ans= (num[p-1]+num[p])/2
            return ans
        
