class MinStack:
     #observation: for every element in stack, we need to know the min
    #min includes current element and all elements before it in the stack
    #idea: use a tuple of (val, minVal)

    #TC: O(1) for all operations, SC: O(N), need to maintain 2 stacks
    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        #find minVal and append
        minVal = min(val, self.getMin()) if len(self.stack) > 0 else val
        self.stack.append( (val, minVal) )

    def pop(self) -> None:
        if len(self.stack) == 0:
           return None 
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
