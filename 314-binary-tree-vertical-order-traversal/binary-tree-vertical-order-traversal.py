# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        a = {}

        c = 0

        stack = deque([(root, 0)])

        while(stack):
            ele = stack.popleft()
            root = ele[0]
            c = ele[1]

            if root is None:
                continue
            if c in a:
                a[c].append(root.val)
            else:
                a[c] = [root.val]
            stack.append((root.left, c - 1))
            stack.append((root.right, c + 1))
        
            
            
        # def helper(root, c, a):
        #     if root is None:
        #         return
        #     if c in a:
        #         a[c].append(root.val)
        #     else:
        #         a[c] = [root.val]
            
        #     helper(root.left, c-1, a)
        #     # c += 1
        #     helper(root.right, c+1, a)
        
        # helper(root, 0, a)

        return [a[i] for i in sorted(a.keys())]