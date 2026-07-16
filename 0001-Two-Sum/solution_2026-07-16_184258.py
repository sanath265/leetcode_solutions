class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i, v in enumerate(nums):
            numsDict[v] = i
        
        for i, v in enumerate(nums):
            if target - v in numsDict and i != numsDict[target - v]:
                return [i, numsDict[target - v]]