class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []

        def dfs(s, path):
            if not s:
                output.append(path.copy())
                return
            
            for i in range(len(s)):
                if s[:i+1] == s[:i+1][::-1]:
                    path.append(s[:i+1])
                    dfs(s[i+1:], path)
                    path.pop()
        
        dfs(s, [])

        return output