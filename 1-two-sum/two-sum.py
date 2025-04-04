class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = {}
        for i in range(len(nums)):
            nums1[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in nums1 and i != nums1[target - nums[i]]:
                return [i, nums1[target - nums[i]]]
        