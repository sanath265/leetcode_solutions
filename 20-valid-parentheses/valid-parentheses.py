class Solution:
    def isValid(self, s: str) -> bool:
        ope = {"(":")", "[":"]", "{": "}"}
        close = {')':'(', ']':'[', '}': '{'}

        stack = []

        for i in s:
            if i in ope:
                stack.append(i)
            
            else:
                # print(stack, i)
                if not stack:
                    return False
                if stack[-1] == close[i]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True