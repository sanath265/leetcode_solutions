import math
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        # nums.sort()
        # print(nums)
        for i in nums:
            c = 0
            d = 0
            
            for j in range(1, int(i**0.5) + 1):
                if i % j == 0:
                    q = i//j
                    if j == q:
                        c += 1
                        d += j
                    else:
                        c += 2
                        d += j + q
                if c > 4:
                    break
                    
            if c == 4:
                # print(i)
                ans += d

        return ans
                


        