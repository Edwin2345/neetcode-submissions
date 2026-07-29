class MinStack:
    #idea, use 1 stakc but insert a tuple of (val, min) every time
    #min is min(val, all prev val)
    def __init__(self):
        self.stack = []    

    def push(self, val: int) -> None:
        if len(self.stack) > 0:
           minVal = min(val, self.stack[-1][1])
           self.stack.append((val, minVal))
        else:
           self.stack.append((val, val))  
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
        
