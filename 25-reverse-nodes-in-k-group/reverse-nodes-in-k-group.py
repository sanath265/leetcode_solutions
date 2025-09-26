# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k <= 1 or head is None:
            return head
        
        dummy = ListNode(0)
        prev = dummy
        prev.next = head

        temp = head
        end = head

        while(temp):
            count = 1
            while(end.next and count < k):
                count += 1
                end = end.next
            if count != k:
                return dummy.next

            prev.next = None
            tail = end.next
            end.next = None

            print(temp, end)

            prevSmall = None
            curr = temp
            while(curr):
                nex = curr.next
                curr.next = prevSmall
                prevSmall = curr
                curr = nex
            
            print(temp, prevSmall)
            
            prev.next = prevSmall
            temp.next = tail

            prev = temp
            temp = temp.next
            end = temp
        
        return dummy.next
            


        