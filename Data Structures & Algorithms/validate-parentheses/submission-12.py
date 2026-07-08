class Solution:
   def isValid(self, s: str) -> bool:
    open_brac = []

    if len(s) % 2 != 0:
        return False

    for char in s:
        if char == "}":
            if len(open_brac) == 0:
                return False
            
            elif open_brac.pop() != "{":
                return False

        elif char == "]":
            if len(open_brac) == 0:
                return False
            
            elif open_brac.pop() != "[":
                return False

        elif char == ")":
            if len(open_brac) == 0:
                return False
            
            elif open_brac.pop() != "(":
                return False

        else:
            open_brac.append(char)
    
    if len(open_brac) == 0:
        return True
    
    else:
        return False
