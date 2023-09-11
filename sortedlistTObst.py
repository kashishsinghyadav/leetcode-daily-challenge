# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        temp=head
        lst=[]
        while temp:
            lst.append(temp.val)
            temp=temp.next
        print(temp)

        def dfs(l,r):
            if l>r:
                return None
            mid=(l+r)//2

            root=TreeNode(lst[mid])
            root.left=dfs(l,mid-1)
            root.right=dfs(mid+1,r)
            return root

        return dfs(0,len(lst)-1)
        
