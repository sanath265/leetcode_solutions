class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums.sort()
        num = 1
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2
        for i in nums:
            if i >= num * 2:
                num *= 2
        
        
        return num + num


        