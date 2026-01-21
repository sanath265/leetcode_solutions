class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for i in nums:
            if i == 2:
                ans.append(-1)
                continue

            d = 0

            while((i & (1<<d)) != 0):
                d += 1
            
            ans.append(i - (1<<d-1))
        return ans