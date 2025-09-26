# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        fast = head

        dummy = ListNode(0)
        temp = dummy
        while(fast and fast.next and fast.next.next):
            mid = fast.next
            nex = fast.next.next
            fast.next = None
            mid.next = None

            fast.next = nex
            temp.next = mid
            fast = fast.next
            temp = temp.next
            # print(fast, temp)

        
        if fast.next:
            temp.next = fast.next
            fast.next = None
        
        fast.next = dummy.next
        return head
            
        