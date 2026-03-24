class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0

        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "0"
                for x, y in dir:
                    dfs(i+x, j+y)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # print(grid, i, j)
                    islands += 1
                    dfs(i, j)
        return islands
            

        