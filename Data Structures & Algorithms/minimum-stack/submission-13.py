class MinStack:
    #prute force, search entire stakc to find min
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        if len(self.stack) == 0:
           raise ValueError("stack is empty")
        self.stack.pop() 
        
    def top(self) -> int:
        if len(self.stack) == 0:
           raise ValueError("stack is empty")
        return self.stack[-1]
        
    def getMin(self) -> int:
        if len(self.stack) == 0:
           raise ValueError("stack is empty")

        minVal = float("inf")
        for n in self.stack:
            minVal = min(minVal, n)
        return minVal

        
