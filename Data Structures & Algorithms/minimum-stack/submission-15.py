class MinStack:
    #observation: for every element in stack, we need to know the min
    #min includes current element and all elements before it in the stack
    #idea: use a tuple of

    #TC: O(1) for all operations, SC: O(N), need to maintain 2 stacks
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
      #add min entry
        if len(self.stack) == 0:
           self.min_stack.append(val)
        else:
           self.min_stack.append(min(val, self.getMin())) 
        
        #add to stack
        self.stack.append(val)
        
    def pop(self) -> None:
        #pop from both stacks
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
