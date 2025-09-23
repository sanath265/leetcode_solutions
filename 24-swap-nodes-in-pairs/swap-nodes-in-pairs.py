# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        temp = head

        while(temp and temp.next):
            temp1 = temp.next
            end = temp1.next if temp1.next else None
            temp1.next = None
            
            currNext = temp.next
            temp.next = prev
            currNext.next = temp
            prev.next = currNext
            temp.next = end


            if temp.next and temp.next.next:
                prev = temp
                temp = temp.next
            else:
                temp = temp.next
        return dummy.next