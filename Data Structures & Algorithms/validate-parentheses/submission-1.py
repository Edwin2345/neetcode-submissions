class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        parenStack = []

        for letter in s:
            if letter in parenMap:
                parenStack.append(letter)
            elif len(parenStack)==0 or parenMap[parenStack[len(parenStack)-1]] != letter:
                return False
            else:
                parenStack.pop()
                
        return len(parenStack) == 0
        