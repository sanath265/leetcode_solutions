class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        nums2 = nums[1:]
        nums2.sort()
        return nums[0] + nums2[0] + nums2[1]