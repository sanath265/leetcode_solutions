# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        c = 0

        if root is None:
            return 0
        
        c = max(c, self.depth(root.left) + self.depth(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return c
        
    @lru_cache(maxsize=None)
    def depth(self, root):

        c = 0

        if root is None:
            return 0
        
        c += 1 + max(self.depth(root.left), self.depth(root.right))

        return c