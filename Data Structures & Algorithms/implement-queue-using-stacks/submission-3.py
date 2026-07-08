class MyQueue:
    """
    s1: 1        -> add fist element to s1, and rest to s2
    s2: 2,3,4,5

    s1: 5,4,3,2  -> pop form s1 then transfer s2 to s1
    s2: 

    s1: 5,4,3,2 ->
    s2: 6

    s1: 5,4,3,2 
    s2: 6,7

    idea: alwasy keep s1 as correctly ordered top stack
         once s1 is empty, pop and push elements of s2 into s1

         push:  if s1 has no element, add to s1
                if it does, put into s2
        
         pop: if s1 empty, move all elements from s2 into s1,then pop from s1
              if s1 has elements, pop and if now empty, move any elements from s2 to s1
    """

    def __init__(self):
        self.s1 = []
        self.s2 = []

        
    def push(self, x: int) -> None:
        if len(self.s1) == 0:
           self.s1.append(x)
        else:
           self.s2.append(x) 

    def transferS2toS1(self):
        while len(self.s2) > 0:
           val = self.s2.pop() 
           self.s1.append(val) 

    def pop(self) -> int:
        if self.empty():
           raise ValueError("queue is empty")
        #if s1 is empty, move over s2 then pop
        elif len(self.s1) == 0:
            self.transferS2toS1()
            return self.s1.pop()
        #if not, get the top of s1, and if empty move everything over
        else:
            firstEl = self.s1.pop()
            if len(self.s1) == 0:
               self.transferS2toS1()
            return firstEl
    
    def peek(self) -> int:
        #return last element of correctly ordered s1
        if self.empty():
            raise ValueError("queue is empty")
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()