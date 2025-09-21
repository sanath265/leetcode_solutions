class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 1:
            return nums[0] + k
        
        missing = nums[-1] - nums[0] + 1 - len(nums)

        totalNums = nums[-1] - nums[0] + 1

        if missing < k:
            return nums[-1] + k - missing
        
        l = 0
        r = len(nums) - 1

        while(l < r):
            mid = r - (r-l) //2

            if nums[mid] - nums[0] - mid < k:
                l = mid
            else:
                r = mid - 1
        
        return nums[0] + l + k

