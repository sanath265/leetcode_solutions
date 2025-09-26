# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def helper(root, minimum, maximum):
            if not root:
                return True
            if root.val > minimum and root.val < maximum:
                return helper(root.left, minimum, root.val) and helper(root.right, root.val, maximum)
            return False
        
        return helper(root, float('-inf'), float('inf'))