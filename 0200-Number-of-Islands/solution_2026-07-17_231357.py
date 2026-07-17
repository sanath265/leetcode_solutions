class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]

        def bfs(i, j):

            if i<0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            for m,n in directions:
                bfs(i+m, j+n)
        

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        
        return count
