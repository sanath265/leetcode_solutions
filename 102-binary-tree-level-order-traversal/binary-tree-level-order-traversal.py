# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        c = []

        if root is None:
            return c
        
        def dfs(root, level):
            if len(c) < level:
                c.append([root.val])
            else:
                # print(c, root.val, level)
                c[level - 1].append(root.val)
            
            for i in [root.left, root.right]:
                if i is not None:
                    dfs(i, level+1)
        dfs(root, 1)

        return c
        d = []

        for i in c:
            d += i
        return d