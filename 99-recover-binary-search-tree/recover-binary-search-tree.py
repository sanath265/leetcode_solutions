# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        violated1 = None
        violated2 = None
        violated3 = None
        prev = None

        def inorder(root):
            nonlocal violated1
            nonlocal violated2
            nonlocal violated3
            nonlocal prev

            if root is None:
                return
            inorder(root.left)

            if prev != None and root.val < prev.val:

                if violated1 is None:
                    violated1 = prev
                    violated2 = root
                
                else:
                    violated3 = root

            prev = root
            inorder(root.right)
        
        inorder(root)

        print(violated1, violated2, violated3)

        if violated3:
            violated3.val, violated1.val = violated1.val, violated3.val
        else:
            violated2.val, violated1.val = violated1.val, violated2.val
        
        return root
        