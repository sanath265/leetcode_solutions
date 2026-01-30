class Solution:
    def jump(self, nums: List[int]) -> int:

        dp = [float('inf') for _ in nums]
        if len(nums) == 1:
            return 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= len(nums) - 1:
                dp[i] = 1
            else:
                dp[i] = min(dp[i:i+nums[i] + 1]) + 1
        # print(dp)
        return dp[0]