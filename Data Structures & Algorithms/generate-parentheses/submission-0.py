class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        validParens = []
        
        def genAllParens(parens, numOpen, numClose):
            #made a valid paren string
            if numOpen == numClose == n:
               validParens.append( "".join(parens) )
               return

            #if we are under n, we can always add an opening
            if numOpen < n:
               parens.append("(")
               genAllParens(parens, numOpen + 1, numClose)
               parens.pop()
            
            #if numClose < numOpen -> it is valid to add a closing
            if numClose < numOpen:              
               parens.append(")")
               genAllParens(parens, numOpen, numClose + 1) 
               parens.pop()
            
        genAllParens([],0,0)
        return validParens
        