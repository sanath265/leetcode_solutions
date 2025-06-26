class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 2**31

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.stack.append([val, self.min])

    def pop(self) -> None:
        if len(self.stack) != 0:
            self.stack.pop()
        
        if len(self.stack) != 0:
            self.min = self.stack[-1][1]
        else:
            self.min = 2**31

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()