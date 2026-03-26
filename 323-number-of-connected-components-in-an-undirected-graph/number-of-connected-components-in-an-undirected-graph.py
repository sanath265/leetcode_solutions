class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = [0 for _ in range(n)]

        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(i):
            if visited[i]:
                return
            
            visited[i] = 1

            for i in adj[i]:
                dfs(i)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count+=1
                dfs(i)
        return count

