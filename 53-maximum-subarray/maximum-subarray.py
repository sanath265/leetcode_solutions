class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        m = -float('inf')
        s = 0
        for i in nums:
            s = max(i, s + i)
            m = max(m, s)
        return m