# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        left = self.depth(root.left)
        right = self.depth(root.right)

        # isBalanced(root.left)
        # isBalanced(root.right)
        return (abs(right - left) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right))
    
    def depth(self, root):
        c = 0

        if root is None:
            return 0

        c += 1 + max(self.depth(root.left), self.depth(root.right))

        return c