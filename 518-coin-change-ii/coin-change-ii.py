class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = {}

        def dfs(i, amount):
            res = 0

            if i == len(coins):
                return 0
            
            if (i, amount) in dp:
                return dp[(i, amount)]
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            
            res = dfs(i, amount - coins[i]) + dfs(i+1, amount)
            
            dp[(i, amount)] = res
            return res
        return dfs(0, amount)
