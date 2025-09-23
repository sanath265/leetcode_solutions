# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        l = None
        for i in range(a - 1):
            list1 = list1.next
        l = list1
        r = l
        for i in range(b-a + 2):
            r = r.next
        
        m = list2

        while(m.next != None):
            m = m.next
        
        if l == None:
            m.next = r
            return list2
        
        l.next = list2
        m.next = r
        return temp
            