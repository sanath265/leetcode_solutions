class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        
        dp = {}
        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i,j)]

            if i ==0 and j == 0:
                dp[(i,j)] = poured
                return poured
            
            if i < 0 or j < 0 or i >=100 or j >= 100:
                return 0
            
            dp[(i,j)] = max(0, dfs(i-1, j-1) - 1) / 2 + max(0, dfs(i-1 , j) - 1) / 2

            return dp[(i,j)]
        
        ans = min(1, dfs(query_row, query_glass))
        print(dp)
        return ans
        


