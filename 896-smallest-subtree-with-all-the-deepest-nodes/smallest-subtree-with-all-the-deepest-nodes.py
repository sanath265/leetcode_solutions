# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        a = {}

        queue = deque([(root, 1)])
        
        level = 1

        maxLevel = 0
        while(queue):
            val = queue.popleft()
            root1 = val[0]
            currLevel = val[1]
            if root1.left:
                queue.append((root1.left, currLevel + 1))
                a[root1.left] = [root1, currLevel + 1]
                maxLevel = currLevel + 1
            
            if root1.right:
                queue.append((root1.right, currLevel + 1))
                a[root1.right] = (root1, currLevel + 1)
                maxLevel = currLevel + 1

        c = []
        for i in a:
            if a[i][1] == maxLevel:
                c.append(i)
        # print(c)
        if len(c) == 1:
            return c[0]
        elif len(c) == 0:
            return root
        
        d = set(c)
        f = set(c)
        while(f):
            print(f)
            if len(f) == 1:
                return f.pop()
            d = f
            f = set()
            while(d):
                root = d.pop()
                f.add(a[root][0])
