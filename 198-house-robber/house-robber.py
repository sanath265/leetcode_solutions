class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def rec(i, mem, nums):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if mem[i] > -1:
                return mem[i]
            
            mem[i] = max(rec(i-1, mem, nums), nums[i] + rec(i-2, mem, nums))

            return mem[i]
        
        return rec(len(nums) - 1, [-1 for _ in nums], nums)
            