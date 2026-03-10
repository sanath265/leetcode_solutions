class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort()

        dp = [[-1 for _ in range(len(pairs) + 1)] for _ in pairs]
        def dfs(i, prev):
            res = 0

            if i == len(pairs):
                return 0
            
            if dp[i][prev+1] != -1:
                return dp[i][prev+1]
            
            take = 0
            if prev == -1 or pairs[prev][1] < pairs[i][0]:
                take = 1 + dfs(i+1, i)
            
            skip = dfs(i+1, prev)

            res = max(take, skip)

            dp[i][prev+1] = res

            return res
        
        return dfs(0, -1)