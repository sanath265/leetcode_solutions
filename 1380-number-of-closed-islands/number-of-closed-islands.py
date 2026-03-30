class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        directions = [(0,1), (0, -1), (1,0), (-1, 0)]
        def dfs(i, j):
            if i >=0 and j >= 0 and i < row and j < col and  grid[i][j] == 0:
                grid[i][j] = 1
                for x, y in directions:
                    dfs(i+x, j+y)
        
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0 or i == row - 1 or j == col -1:
                        dfs(i, j)
        c = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    dfs(i, j)
                    c+=1
        return c




        