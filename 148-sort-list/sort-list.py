# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        
        return self.split(head)
    

    def split(self, head):
        fast = head
        slow = head

        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
        
        l = None
        r = None
        if fast == slow:
            nex = fast.next
            fast.next = None
            l = fast
            r = nex
        else:
            nex = slow.next
            slow.next = None
            l = self.split(head)
            r = self.split(nex)
        # print(l, r)
        return self.merge(l, r)

    def merge(self, l, r):
        # print("before", l, r)
        dummy = ListNode(0)
        temp = dummy
        while(l and r):
            if l.val < r.val:
                temp.next = l
                temp = temp.next
                l = l.next
                temp.next = None
            else:
                temp.next = r
                temp = temp.next
                r = r.next
                temp.next = None
        if l:
            temp.next = l
        else:
            temp.next = r
        
        # print("after", dummy.next)
        return dummy.next
        

