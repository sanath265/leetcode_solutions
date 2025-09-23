# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        prev = head
        curr = head.next

        c = 1
        d = []
        while(curr.next):
            if (prev.val < curr.val and curr.val > curr.next.val) or (prev.val > curr.val and curr.val < curr.next.val):
                d.append(c)
            prev = curr
            curr = curr.next
            c+=1
        
        if len(d) < 2:
            return [-1, -1]
        else:
            minim = float('inf')

            for i in range(1, len(d)):
                minim = min(minim, d[i] - d[i-1])

            return[minim, d[-1] - d[0]]
