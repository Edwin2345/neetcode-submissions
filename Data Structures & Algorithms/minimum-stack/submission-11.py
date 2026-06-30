class MinStack:
    def __init__(self):
        self.stack = []  
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minStack.append(val)
        
        elif self.minStack[-1] >= val:
            self.minStack.append(val)

        self.stack.append(val)
        
    def pop(self) -> None:
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
