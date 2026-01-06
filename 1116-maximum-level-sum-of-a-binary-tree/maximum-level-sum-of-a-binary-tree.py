# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = deque([(root, 1)])
        maxi = root.val
        level = 1
        maxLevel = 1
        count = 0

        while(queue):
            val = queue.popleft()
            # print(val)
            root = val[0]
            currLevel = val[1]
            if currLevel == level:
                count += root.val
            else:
                level += 1
                if count > maxi:
                    maxi = count
                    print(maxi)
                    maxLevel = currLevel - 1
                count = root.val
            print(root.val, currLevel, count)
            if root.left:
                queue.append((root.left, currLevel + 1))
            if root.right:
                queue.append((root.right, currLevel + 1))
        
        # print(count, maxi, currLevel)
        if count > maxi:
            maxi = count
            # print(maxi)
            maxLevel = currLevel
        return maxLevel
            
            


        