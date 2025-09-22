# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        l = None
        r = None
        temp = list1
        for i in range(a-1):
            list1 = list1.next
        
        l = list1

        for i in range(b - a + 1):
            list1 = list1.next
        r = list1.next

        if a == 0:
            list2.next = r
            return list2
        
        l.next = list2

        while(l.next != None):
            l = l.next
        l.next = r

        return temp

