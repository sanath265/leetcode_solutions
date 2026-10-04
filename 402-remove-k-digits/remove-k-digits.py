class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for i in num:
            
            while(stack and stack[-1] > i and k > 0):
                stack.pop()
                k-=1
            
            if not stack and i == "0":
                continue
            stack.append(i)
        
        while(k and stack):
            stack.pop()
            k-=1
        

        if not stack:
            return "0"
        return "".join(stack)

        
        