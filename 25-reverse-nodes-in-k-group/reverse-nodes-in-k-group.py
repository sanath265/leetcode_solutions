# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head

        temp = head

        prev = dummy

        while(temp):
            curr = temp
            end = temp

            count = 1

            while(count < k and end.next):
                count += 1
                end = end.next
            
            if count != k:
                return dummy.next
            
            tail = end.next
            end.next = None
            prev.next = None
            # print(curr, end, tail)

            end = self.reverseList(curr)

            # print(curr, end)

            prev.next = end
            curr.next = tail

            temp = tail
            prev = curr
        
        return dummy.next



    def reverseList(self, head):
        temp = head
        prev = None
        while(temp):
            nex = temp.next
            temp.next = prev
            prev = temp
            temp = nex
        # print(prev)
        return prev
