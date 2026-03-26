class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = [0 for _ in range(n)]

        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i, parent):

            if visited[i]:
                return False
            
            visited[i] = 1

            for node in adj[i]:
                if node != parent:
                    if not dfs(node, i):
                        return False
            
            return True
        
        ans = dfs(0, -1)

        if not ans:
            return ans
        
        for i in visited:
            if not i:
                return False
        
        return ans
        