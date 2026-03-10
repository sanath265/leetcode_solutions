class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # c = 0
        dp = {}

        def dfs(i, target, chain):

            c = 0

            if (i, target) in dp:
                return dp[(i, target)]

            if i == len(nums):
                if target == 0:
                    return 1
                return c

            c += dfs(i+1, target - nums[i], chain + "+")
            c += dfs(i+1, target + nums[i], chain + "-")

            dp[(i, target)] = c

            return c

        return dfs(0, target, "")
        #  c
        
