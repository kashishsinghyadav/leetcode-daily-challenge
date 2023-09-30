class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]

        nums=nums[::-1]
        mini=-1e9
        for n in nums:
            if n<mini:
                return True

            while stack and n >stack[-1]:
                mini=stack.pop()
            stack.append(n)
        return False
