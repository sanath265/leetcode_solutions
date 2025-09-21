# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right or head == None:
            return head

        temp = head
        l = None
        for i in range(left - 1):
            l = temp
            temp = temp.next
        
        prev = None
        nex = None
        for i in range(left, right + 1):
            nex = temp.next
            temp.next = prev
            prev = temp
            temp = nex
        
        if l != None:
            l.next = prev
        else:
            l = prev
        

        if nex != None:
            while(l.next != None):
                l = l.next
            
            l.next = nex
        return prev if left==1 else head
