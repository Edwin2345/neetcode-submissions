class MinStack:
    def __init__(self):
        self.stack = []  

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        self.min_num = self.stack[0]

        for num in self.stack:
            if self.min_num > num:
                self.min_num = num
        
        return self.min_num
