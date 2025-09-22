class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(arr):
            if len(arr) == len(nums):
                output.append(arr.copy())
                return
            for i in nums:
                if i not in arr:
                    arr.append(i)
                    dfs(arr)
                    arr.pop()
        dfs([])

        return output