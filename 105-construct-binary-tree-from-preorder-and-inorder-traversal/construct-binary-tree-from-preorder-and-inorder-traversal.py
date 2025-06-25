# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inHash = {}

        for i, v in enumerate(inorder):
            print
            inHash[v] = i
        
        
        return self.buildtree(inorder, preorder)
        
    def buildtree(self, inorder, preorder):
        if len(preorder) <=0:
            return None

        inHash = {}
        for i, v in enumerate(inorder):
            print
            inHash[v] = i
        
        # print(inorder, preorder)
        root = TreeNode(preorder[0])
        i = inHash[preorder[0]]
        lInorder = inorder[:i]
        rInorder = inorder[i+1:]

        lpreorder = preorder[1:len(lInorder)+1]
        rpreorder = preorder[len(lInorder)+1:]

        root.left = self.buildtree(lInorder, lpreorder)
        root.right = self.buildtree(rInorder, rpreorder)

        return root
