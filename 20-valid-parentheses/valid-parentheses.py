class Solution:
    def isValid(self, s: str) -> bool:
        ope = {"(":")", "[":"]", "{": "}"}

        stack = []

        for i in s:
            if i in ope:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                l = stack.pop()
                print(l)
                if ope[l] == i:
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
