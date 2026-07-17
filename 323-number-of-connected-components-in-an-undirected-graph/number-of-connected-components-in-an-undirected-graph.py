class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = [0 for _ in range(n)]

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        def dfs(node):
            if visited[node] == 1:
                return
            
            visited[node] = 1

            for neigh in adj[node]:
                dfs(neigh)
        
        count = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                count += 1
        
        return count