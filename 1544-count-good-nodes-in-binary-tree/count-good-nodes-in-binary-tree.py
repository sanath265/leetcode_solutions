# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        c = []

        if root is None:
            return len(c)
        
        def dfs(root, maximum):
            if root.val >= maximum:
                c.append(1)
            
            for i in [root.left, root.right]:
                if i is not None:
                    dfs(i, max(root.val, maximum))

        dfs(root, -10001)

        return len(c)