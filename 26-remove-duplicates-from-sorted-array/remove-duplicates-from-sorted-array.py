class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = 0

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                d += 1
                nums[d] = nums[i]
            # else:
                
        return d + 1

