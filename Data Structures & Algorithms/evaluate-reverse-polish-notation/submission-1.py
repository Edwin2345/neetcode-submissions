class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for t in tokens:
            if t in operators:
               p2 = stack.pop()
               p1 = stack.pop()
               if   t == '+':
                 stack.append(p1 + p2)
               elif t == '-':
                 stack.append(p1 - p2)
               elif t == '*':
                 stack.append(p1 * p2)
               elif t == '/':
                 stack.append(int(float(p1) / p2))    
            else:
                stack.append(int(t))
        
        return stack.pop()