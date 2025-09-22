class Solution:
    def simplifyPath(self, path: str) -> str:
        
        files = path.split("/")

        stack = []
        for i in files:
            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == "":
                continue
            else:
                stack.append(i)
        
        return "/" + "/".join(stack)

        
