class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small=ListNode(0)
        s=small
        high=ListNode(0)
        h=high
        while head :
            if head.val < x:
                s.next=head
                s=head
                
            else:
                h.next=head
                h=head
            head=head.next
        h.next=None
        s.next=high.next
        return small.next
