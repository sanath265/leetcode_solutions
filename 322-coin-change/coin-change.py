from functools import lru_cache
class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # dp = []

        @lru_cache(None)
        def dfs(i, amount):

                
            if amount == 0:
                return 0
            
            if i < 0 or amount<0:
                return float("inf")
            
            # key= str(i) + str(amount)
                
            # if key in dp:
            #     return dp[key]
                
            res = float("inf")
            
            res=min(res,1+dfs(i, amount - coins[i]))
            res=min(res,dfs(i-1, amount))
            
            # for coin in range((amount // coins[i]) + 1):
            #     res = min(coin + dfs(i-1, amount - coins[i] * coin), res)
            # dp[key] = res
            return res
        
        
        res = dfs(len(coins) - 1, amount)
        
        if res == float("inf"):
            return -1
        else:
            return res
                
                
                
                
        