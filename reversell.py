# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev,first=dummy,head
        for i in range(left-1):
            prev,first=first,first.next

        p=None
        for i in range(right-left+1):
            temp=first.next
            first.next=p
            p,first=first,temp

        
        prev.next.next=first
        prev.next=p

        return dummy.next
