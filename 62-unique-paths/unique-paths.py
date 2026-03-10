class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {}
        def dfs(i, j):

            ans = 0
            if i == m or j == n:
                return 0
            
            if (i, j) in dp:
                return dp[(i,j)]
            
            if i == m-1 and j == n-1:
                return 1
            
            ans += dfs(i+1, j) + dfs(i, j+1)
            
            dp[(i,j)] = ans
            return ans
        return dfs(0, 0)
        