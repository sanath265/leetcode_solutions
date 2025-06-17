class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        result = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    result = max(self.dfs(i, j, grid), result)
        return result
    
    def dfs(self, i, j, grid):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0

        return (1 + self.dfs(i-1, j, grid) 
        + self.dfs(i+1, j, grid)
        + self.dfs(i, j-1, grid)
        + self.dfs(i, j+1, grid))