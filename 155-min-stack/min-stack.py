class MinStack:
    """
    For a stack, push, pop, and top can be done in O(1) wihtou extra logic
    for getMin(), to have O(1) while appending every number to stack we keep track of min.

    """
    def __init__(self):
        self.stack = []    
        self.min = []
    def push(self, value: int) -> None:
        if not self.min:
            self.stack.append(value)
            self.min.append(value)
        else:
            self.min.append(min(value, self.min[-1]))
            self.stack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()