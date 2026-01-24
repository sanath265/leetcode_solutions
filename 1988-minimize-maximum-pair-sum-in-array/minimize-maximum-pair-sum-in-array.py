class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        l = 0
        r = len(nums) - 1
        while(l < r):
            ans = max(ans, nums[l] + nums[r])
            l+=1
            r -=1
        return ans