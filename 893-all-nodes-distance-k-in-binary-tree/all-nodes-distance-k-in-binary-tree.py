# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adj = {}

        def traverseRoot(root):
            nonlocal adj
            if root is None:
                return
            val = []

            if root.left:
                val.append(root.left.val)
            if root.right:
                val.append(root.right.val)
            
            if root.val not in adj:
                adj[root.val] = val
            else:
                adj[root.val] += val
            
            if root.left and root.left.val not in adj:
                adj[root.left.val] = [root.val]
            elif root.left:
                adj[root.left.val] += [root.val]

            if root.right and root.right not in adj:
                adj[root.right.val] = [root.val]
            elif root.right:
                adj[root.right.val] += [root.val]
            
            traverseRoot(root.left)
            traverseRoot(root.right)

        traverseRoot(root)

        print(adj)

        res = set()
        visited = {}

        def dfs(node, count):
            if count == k:
                res.add(node)
                return

            if node in visited:
                return
            
            visited[node] = 1

            count += 1

            for i in adj[node]:
                if i not in visited:
                    dfs(i, count)
        
        dfs(target.val, 0)
        a = []

        for i in res:
            a.append(i)
        
        return a