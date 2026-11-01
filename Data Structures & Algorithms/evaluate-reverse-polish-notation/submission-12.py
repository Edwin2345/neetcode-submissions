class Solution:
    #all binary operaters and string is valid aremthtic expression

    def evalRPN(self, tokens: List[str]) -> int:
        opSet = {"+", "-", "*", "/"}
        stack = []

        for t in tokens:
            #parse and add number to stack
            if t not in opSet:
               stack.append(int(t)) 
               continue 

            #otherwise, pop 2 nums from stack, do operation, and add back
            n2 = stack.pop()
            n1 = stack.pop()   
         
            if t == "+":
               stack.append(n1 + n2)
            elif t == "-":
               stack.append(n1 - n2)
            elif t == "*":
               stack.append(n1 * n2)
            elif t == "/":
               stack.append( int(n1 / n2) )
        
        #return final ans
        return stack[0]
            
             