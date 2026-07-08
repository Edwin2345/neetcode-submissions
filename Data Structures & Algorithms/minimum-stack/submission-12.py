class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val):
        self.stack.append(val)

        if len(self.minStack) == 0:
            self.minStack.append(val)
        
        elif self.minStack[-1] >= val:
            self.minStack.append(val)
    
    def pop(self):
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]
