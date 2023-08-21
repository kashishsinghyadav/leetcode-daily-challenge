class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # for n in matrix:
        #     curr=n
        #     if curr[-1]>=target:
        #         if target in curr:
        #             return True
        # return False

        for num in matrix:
            cur=num
            if cur[-1]>=target:
                if target in cur:
                    return True
        return False
