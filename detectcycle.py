class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        pt1=head
        pt2=head
        while pt2 and pt2.next:
            pt1=pt1.next
            pt2=pt2.next.next
            if pt1==pt2:
                return True
        
        return False
