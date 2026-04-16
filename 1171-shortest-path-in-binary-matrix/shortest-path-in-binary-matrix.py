class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        row  = len(grid)
        col = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1

        ans = float("inf")

        heap = []
        heapq.heappush(heap, [1, 0,0])
        
        dist = [[float("inf") for _ in range(col)] for _ in range(row)]
        dist[0][0] = 1

        while heap:
            cost, i, j = heapq.heappop(heap)

            # if dist[i][j] < cost:
            #     continue

            if i == row-1 and j == col-1:
                return cost
                
            dist[i][j] = cost
            for x, y in directions:
                ni = i+x
                nj = j + y
                if ni >= 0 and nj >=0 and ni < row and nj < col and grid[ni][nj]==0:
                    new_cost = cost + 1

                    if new_cost < dist[ni][nj]:
                        dist[ni][nj] = new_cost
                        heapq.heappush(heap, (new_cost, ni, nj))
        
        return -1