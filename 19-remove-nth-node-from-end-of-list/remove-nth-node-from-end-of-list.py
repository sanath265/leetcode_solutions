# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        c = 0

        while(fast.next and fast.next.next):
            fast = fast.next.next
            c += 2
        
        if fast.next:
            c += 2
        else:
            c += 1
        
        node = c - n

        if node == 0:
            return head.next
        
        temp = head
        while(node != 1):
            temp = temp.next
            node -= 1
        
        if temp.next and temp.next.next:
            temp.next = temp.next.next
        else:
            temp.next = None
        
        return head

        