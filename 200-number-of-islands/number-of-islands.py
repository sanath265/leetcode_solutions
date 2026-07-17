class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #BFS

        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        row = len(grid)
        col = len(grid[0])

        def bfs(row1, col1):
            q = deque([(row1, col1)])

            while q:
                i, j = q.popleft()

                for m,n in directions:
                    ni = i+m
                    nj = j+n
                    if ni>= 0 and ni < row and nj >= 0 and nj < col and grid[ni][nj] == "1":
                        grid[ni][nj] = "0"
                        q.append((ni, nj))
            
        
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1

        return count

        #DFS
        # directions = [(0,1), (0,-1), (1,0), (-1, 0)]

        # def dfs(i, j):

        #     if i<0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        #         return
            
        #     if grid[i][j] == "0":
        #         return
            
        #     grid[i][j] = "0"

        #     for m,n in directions:
        #         bfs(i+m, j+n)
        

        # count = 0

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == "1":
        #             count += 1
        #             bfs(i, j)
        
        # return count
