

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# class Solution:
#     def (self, target: int, arr: 'MountainArray') -> int:
        
#         k=arr.index(target)
#         if k:
#             return k
#         return -1
class Solution:

    def findInMountainArray(self, target: int,mountain_arr):
        low = 1
        high = mountain_arr.length() - 2

        while low != high:
            mid = low + (high - low) // 2

            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid

        return low
