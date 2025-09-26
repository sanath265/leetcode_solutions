# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head

        temp = head
        
        prev = dummy
        while(temp and (temp and temp.next)):
            curr = temp
            end = temp.next
            tail = temp.next.next

            end.next = None
            prev.next = None

            rev = self.reverseList(curr)

            prev.next = end
            curr.next = tail

            prev = curr
            temp = tail
        return dummy.next

    
    def reverseList(self, head):
        prev = None

        while(head):
            nex = head.next
            head.next = prev
            prev = head
            head = nex
        
        return prev
            

