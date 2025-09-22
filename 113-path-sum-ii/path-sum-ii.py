# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        paths = []

        def dfs(root, add, path):
            # nonlocal paths
            if root is None:
                return
            print(add, path)
            add += root.val
            path.append(root.val)
            if add == targetSum and not root.left and not root.right:
                paths.append(path[:])
            else:
                dfs(root.left, add, path)
                dfs(root.right, add, path)
            path.pop()
        dfs(root, 0, [])
        return paths