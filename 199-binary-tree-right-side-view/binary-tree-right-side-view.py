# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        c = []

        if root is None:
            return c
        
        def dfs(root, level):
            if level == len(c):
                c.append(root.val)
            
            for i in [root.right, root.left]:
                if i is not None:
                    dfs(i, level+1)
        dfs(root, 0)
        return c        
