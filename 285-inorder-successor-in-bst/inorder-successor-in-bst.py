# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        

        if root is None:
            return None

        answer = None

        def dfs(root):
            nonlocal answer
            if root is None:
                return None

            if p.val < root.val:
                answer = root
                dfs(root.left)
            else:
                dfs(root.right)

        dfs(root)
        return answer
            
