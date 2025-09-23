# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head.next
        l = head
        c = 0
        while(temp):
            if temp.val == 0:
                l.val = c
                c = 0
                if temp.next:
                    l.next = temp
                    l = temp
                else:
                    l.next = None
            else:
                c += temp.val
            
            temp = temp.next
        return head