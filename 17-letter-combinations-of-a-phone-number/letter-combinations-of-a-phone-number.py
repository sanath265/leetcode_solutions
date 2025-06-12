class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        result = []

        def dfs(s, path):
            if not s:
                j = "".join(path.copy())
                if len(j) > 0:
                    result.append("".join(path.copy()))
                return
            for i in phone[s[0]]:
                path.append(i)
                dfs(s[1:], path)
                path.pop()
        dfs(digits, [])

        return result