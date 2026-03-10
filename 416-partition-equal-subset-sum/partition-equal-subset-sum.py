class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        dp = [[-1 for _ in range(total)] for _ in nums]

        def dfs(i, prevSum):
            
            if i == len(nums):
                return prevSum == total - prevSum
            
            if dp[i][prevSum] != -1:
                return dp[i][prevSum]
            

            take = dfs(i+1, nums[i] + prevSum)
            skip = dfs(i+1, prevSum)

            res = take or skip
            dp[i][prevSum] = res
            # print(prevSum)
            return res
        res = dfs(0, 0)

        # print(dp)
        return res
