# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast = head
        slow = head

        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        
        if not fast or not fast.next:
            return None
        
        fast = head

        while(fast != slow):
            fast = fast.next
            slow = slow.next
        
        return fast


