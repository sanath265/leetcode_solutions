class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(pos, total, arr):
            if total == target:
                output.append(arr.copy())
                return
            
            if pos >= len(candidates) or total > target:         
                return

            arr.append(candidates[pos])

            dfs(pos, total + candidates[pos], arr)

            arr.pop()

            dfs(pos + 1, total, arr)
        
        dfs(0, 0, [])

        return output
            
        