class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for t in tokens:
            if t not in operators:        
                stack.append(int(t))
            else:
                o2 = stack.pop()
                o1 = stack.pop()
                if t == "+":
                    stack.append(o1+o2)
                elif t == "-":
                    stack.append(o1-o2)
                elif t == "*":
                    stack.append(o1*o2)
                elif t == "/":
                    stack.append(int(float(o1)/o2))
        
        return stack.pop()