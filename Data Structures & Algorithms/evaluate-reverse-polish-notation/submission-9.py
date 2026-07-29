class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opSet = set(["+", "-", "*", "/"])
        stack = []

        def rpn(i):
            #base case
            if i == len(tokens):
              return stack[0]
           
           #add number to stack
            if tokens[i] not in opSet:
               stack.append(int(tokens[i]))
            else:
               t2 = stack.pop()
               t1 = stack.pop()

               match tokens[i]:
                   case "+":
                      stack.append(t1 + t2)
                   case "-":
                      stack.append(t1 - t2)
                   case "*":
                      stack.append(t1 * t2)
                   case "/":
                      stack.append(int(float(t1)/t2))

            return rpn(i+1)

        return rpn(0)