class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for _ in range(m)]

        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = min(dp[j-1][i] + grid[j][i], dp[j][i-1] + grid[j][i])
        
        # print(dp)
        return dp[m-1][n-1]