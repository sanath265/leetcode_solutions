class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        adj = {}

        for i, j, score in roads:
            if i not in adj:
                adj[i] = [(j, score)]
            else:
                adj[i].append((j, score))
            
            if j not in adj:
                adj[j] = [(i, score)]
            else:
                adj[j].append((i, score))
        print(adj)
        
        visited = [0 for _ in range(n+1)]
        def dfs(i):
            res = float('inf')
            for neigh, score in adj[i]:
                res = min(res, score)
                if visited[neigh] != 1:
                    visited[neigh] = 1
                    res = min(res, dfs(neigh))

            
            return res
        visited[1] = 1
        return dfs(1)
        