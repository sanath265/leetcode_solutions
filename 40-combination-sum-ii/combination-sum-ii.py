class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        def dfs(start, total, arr):
            if total == 0:
                output.append(arr.copy())
                return
            if total < 0:
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if total < candidates[i]:
                    break

                arr.append(candidates[i])
                dfs(i+1, total - candidates[i], arr)
                arr.pop()

        
        candidates.sort()

        dfs(0, target, [])
        
        return output