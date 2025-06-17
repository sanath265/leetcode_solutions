class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row = len(grid)
        col = len(grid[0])

        islands = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    islands += 1
                    self.dfs(i, j, grid)
        return islands
        

    def dfs(self, row, col, grid):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1":
                return
            i = row
            j = col

            grid[i][j] = "0"

            self.dfs(i+1, j, grid)
            self.dfs(i-1, j, grid)
            self.dfs(i, j+1, grid)
            self.dfs(i, j-1, grid)

            return grid
