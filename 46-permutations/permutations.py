class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        visited = [0 for _ in range(n)]

        def dfs(arr):
            if len(arr) == n:
                output.append(arr.copy())
            
            
            for num in nums:
                if num not in arr:
                    arr.append(num)
                    dfs(arr)
                    arr.pop()
  
        dfs([])

        return output
            
