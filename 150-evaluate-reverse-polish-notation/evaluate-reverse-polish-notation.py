class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        def calculate(a, b, operator):
            match operator:
                case "+":
                    return a+b
                case "-":
                    return a - b
                case "*":
                    return a * b
                case "/":
                    return int(a / b)
                case _:
                    return -1

        for i in tokens:
            if i == "+" or i == "-" or i == "/" or i == "*":
                # print(stack)
                num1 = stack.pop()
                num2 = stack.pop()
                # print(6//-132)
                stack.append(calculate(num2, num1, i))
            else:
                stack.append(int(i))
            
        return stack[0]
                
        


        