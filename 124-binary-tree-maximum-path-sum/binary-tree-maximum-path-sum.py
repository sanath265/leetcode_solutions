# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        m = -float('inf')

        def dfs(root):
            nonlocal m

            if root is None:
                return 0

            l = max(0, dfs(root.left))
            r = max(0, dfs(root.right))

            m = max(m, root.val + l + r)

            return max(root.val + l, root.val + r)
        
        dfs(root)
        return m
        