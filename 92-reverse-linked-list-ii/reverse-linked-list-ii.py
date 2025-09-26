# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        temp = dummy

        for i in range(left - 1):
            temp = temp.next
        
        l = temp
        curr = temp.next
        l.next = None

        end = curr
        for i in range(right - left):
            end = end.next
        
        tail = end.next

        end.next = None

        # print(l, curr, tail)

        
        
        revers = self.reverseList(curr)

        print(revers)

        l.next = revers
        print(l, curr)
        curr.next = tail
        
        return dummy.next
    
    def reverseList(self, head):
            prev = None
            while(head):
                nex = head.next
                head.next = prev
                prev = head
                head = nex
            
            return prev
