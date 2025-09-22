# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        prev = None
        curr = head

        while(curr):
            if curr.val == val:
                if prev == None:
                    curr = curr.next
                    head = curr
                    # print(curr)
                else:
                    prev.next = curr.next
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return head