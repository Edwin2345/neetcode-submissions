#Q: is empty string valid
#P: need to map opening brackt to closing sow e know there a pair
#Idea: use a stack, iterat throguh chars, 
#       1. if opening bracket -> add to stack
#       2. if mis match clsoing bracket fcompare dto topp of stack -> pop both
#       3. if matching close brack with top of stack -> pop stack
#       4. return true if len(stakc) == 0 (all matched and poped) else false
    
class Solution:
    def isValid(self, s: str) -> bool:
        #assume empty string is valid
        if len(s) == 0:
           return True 
        
        #declare variables
        bracketMap = {"{" : "}", "[" : "]", "(" : ")"}
        stack = []        

        for ch in s:
            #add opening
            if ch in bracketMap:
               stack.append(ch)
            #matchign closing
            elif stack and bracketMap[stack[-1]] == ch:
               stack.pop()
            #mismatch closing
            else:
                return False
        
        return len(stack) == 0
        