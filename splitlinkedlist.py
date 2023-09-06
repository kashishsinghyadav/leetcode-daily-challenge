# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l=0
        temp=head
        while temp:
            l+=1
            temp=temp.next

        temp=head
        no_of_part=l//k
        rem=l%k
        res=[]

        for i in range(k):
            lst=no_of_part+1 if i<rem else no_of_part
            if lst==0:
                res.append(None)
            else:
                lst1=temp
                for _ in range(lst-1):
                    temp=temp.next

                newnode=temp.next
                temp.next=None
                res.append(lst1)
                temp=newnode

        return res
