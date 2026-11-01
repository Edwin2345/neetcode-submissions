class Solution:
    # this is a problem were we process current char based on previous
    # and we need all previous char to be processed aswell --> stack
    def isValid(self, s: str) -> bool:
        openStack = []
        bracketMap = {"(": ")", "[": "]", "{": "}"}

        #iterate through characters in string
        for ch in s:
            # opening parens we push onto stack
            if ch in bracketMap.keys():
                openStack.append(ch)
            # otherwise check if closing matches the top of open bracket stack
            elif len(openStack) == 0 or bracketMap[openStack[-1]] != ch:
                return False
            #if so, pop from stack
            else:
                openStack.pop()
        
        #check all opening brackets have matching closing
        return len(openStack) == 0
                   
