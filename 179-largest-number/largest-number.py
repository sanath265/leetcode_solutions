from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        def comp(a, b):
            if a+b > b+a:
                return -1
            elif a+b < b+a:
                return 1
            return 0
        
        for i in range(len(nums)):
            mini = i
            for j in range(i+1, len(nums)):
                if comp(nums[mini], nums[j]) >= 0:
                    mini = j
                    # print(nums[mini], nums[i])
            nums[i], nums[mini] = nums[mini], nums[i]
            # print(nums)
        ans = "".join(nums)
        c = 0
        for i in ans:
            if i == '0':
                c+=1
        
        if c == len(ans):
            return "0"

        return "".join(nums)