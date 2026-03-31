# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        c = 0
        def rec(node, t):
            nonlocal c
            if node is None:
                return

            if t + node.val == targetSum:
                print(t, node.val)
                c += 1
            
            rec(node.left, t + node.val)
            rec(node.right, t + node.val)

            

        def count(node):
            if node is not None:
                rec(node, 0)
                count(node.left)
                count(node.right)
        
        count(root)

        return c
            

        