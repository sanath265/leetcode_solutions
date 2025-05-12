class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # if len(nums) == 1:
        #     return nums[0]
        # elif len(nums) == 2:
        #     return max(nums)
        # else:
        #     return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))

        
        dp = [0 for _ in range(len(nums))]

        if len(nums) < 3:
            return max(nums)
        else:
            dp[0] = nums[0]
            dp[1] = max(nums[1], nums[0])

            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            return dp[len(nums) - 1]
