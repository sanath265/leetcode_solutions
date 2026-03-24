"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node, visited):
            newNode = None

            if node in visited:
                return visited[node]
            if node and node not in visited:
                
                newNode = Node(node.val)
                visited[node] = newNode
                neigh = []
                for i in node.neighbors:
                    neigh.append(dfs(i, visited))
                
                newNode.neighbors = neigh

            # if newNode:
            #     print(newNode.val, newNode.neighbors)
            return newNode

        return dfs(node, visited)
        