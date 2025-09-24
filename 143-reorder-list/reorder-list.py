# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head

        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        first = head

        prev = None
        while(second):
            curr = second.next
            second.next = prev
            prev = second
            second = curr
        
        second = prev

        # print(first, second)
        
        # temp = ListNode(0)
        while(second):
            nex = first.next
            first.next = second
            second = second.next
            first = first.next
            first.next = nex
            if first.next:
                first = first.next
        
            # temp.next = first
            # temp = temp.next
            # temp.next = second
            # temp = temp.next
            # second = second.next
            # first = first.next
        
        # if first:
        #     temp.next = first
            
        