# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = ""
        
        stack = deque()
        stack.append(root)
        while (len(stack) > 0):
            root = stack.popleft()
            if root is None:
                s += "-,"
                continue
            else:
                s += str(root.val)+","

            stack.append(root.left)
            stack.append(root.right)

        # print(s)
        return s
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")
        arr.pop()
        # print(arr)

        stack = []
        if arr[0] == "-":
            return None
        
        queue = deque(arr)
        root = TreeNode(int(queue.popleft()))
        stack = deque()
        stack.append(root)

        while(stack):
            node = stack.popleft()

            l = queue.popleft()
            r = queue.popleft()


            if l == "-":
                node.left = None
            else:
                node.left = TreeNode(int(l))
                stack.append(node.left)
            
            if r == "-":
                node.right = None
            else:
                node.right = TreeNode(int(r))
                stack.append(node.right)
            # print(node)
        return root

            

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))