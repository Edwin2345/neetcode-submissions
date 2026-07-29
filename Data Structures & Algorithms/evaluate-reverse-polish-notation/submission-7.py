class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opSet = set(["+", "-", "*", "/"])
        stack = []

        for t in tokens:
            #add nuemric value
            if t not in opSet:
               stack.append(int(t))
               continue
            
            #get two operands
            t2 = stack.pop()
            t1 = stack.pop()

            #apply operation and append result
            if t == "+":
               stack.append(t1 + t2)
            elif t == "-":
               stack.append(t1 - t2)
            elif t == "*":
                stack.append(t1 * t2)
            elif t == "/":
                stack.append(int(float(t1) / t2))

        #top of stack is final value
        return stack[0]