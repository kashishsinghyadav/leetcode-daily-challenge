class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hash={}
        curr=head
        while curr:
            hash[curr]=Node(curr.val)
            print(hash[curr])
            print(curr.val)
            curr=curr.next
        curr=head
        while curr:
            hash[curr].next=hash.get(curr.next)
            hash[curr].random=hash.get(curr.random)
            curr=curr.next
        
        return hash[head]


