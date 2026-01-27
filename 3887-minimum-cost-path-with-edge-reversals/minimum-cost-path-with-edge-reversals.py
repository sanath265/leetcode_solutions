class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = {}
        for i in edges:
            if i[0] not in adj:
                adj[i[0]] = [(i[1], i[2])]
            else:
                adj[i[0]].append((i[1], i[2]))
            
            if i[1] not in adj:
                adj[i[1]] = [(i[0], 2*i[2])]
            else:
                adj[i[1]].append((i[0], 2*i[2]))
        # for i in adj:
            # adj[i].sort()
        print(adj)

        pq = [(0,0)]
        dist = [float('inf') for _ in range(n)]

        while pq:
            # print(pq, dist)
            cost, nex = heapq.heappop(pq)

            if nex not in adj:
                continue
            for v, w in adj[nex]:
                if w + cost < dist[v]:
                    dist[v] = w + cost
                    pq.append((dist[v], v))
        
        if dist[n-1] != float("inf"):
            return dist[n-1]
        else:
            return -1

        

        # def dfs(source, destination, visited):
        #     ans = float('inf')
        #     visited[source] = 1

        #     if source not in adj:
        #         return ans
        #     neighbors = adj[source]

        #     for i in neighbors:
        #         if visited[i[0]] != 1:
        #             if i[0] == destination:
        #                 ans = min(ans, i[1])
        #             else:
        #                 ans = min(i[1] + dfs(i[0], destination, visited), ans)
        #         else:
        #             continue
        #         # print(source, i[0], visited)
        #     visited[source] = 0
        #     return ans
        
        # ans = dfs(0, n-1, [0 for _ in range(n)])

        # if ans == float("inf"):
        #     return -1
        
        # return ans