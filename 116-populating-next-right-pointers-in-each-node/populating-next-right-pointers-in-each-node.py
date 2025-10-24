"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        stack = deque([(root, 0)])

        while stack:

            ele = stack.popleft()

            roo = ele[0]

            count = ele[1]

            if roo == None:
                continue

            if len(stack) == 0:
                roo.next = None
            
            else:
                nex = stack[0]

                if count == nex[1]:
                    roo.next = nex[0]
                else:
                    roo.next = None
            
            stack.append((roo.left, count+1))
            stack.append((roo.right, count+1))

        # print(root)
        return root