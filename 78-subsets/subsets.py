class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def dfs(arr, pos):
            if pos == len(nums):
                subsets.append(arr.copy())
                return

            arr.append(nums[pos])
            dfs(arr, pos + 1)
            arr.pop()
            dfs(arr, pos + 1)

        dfs([], 0)
        return subsets
