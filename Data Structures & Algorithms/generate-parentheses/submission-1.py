class Solution:
    #make a recursive function that tries to add open or closing at current index
    # note: can always add a opening, but can onyl add closing if numOpen > numClose
    def generateParenthesis(self, n: int) -> List[str]:
        allParens = []

        def dfs(parenStr, numOpen, numClosed):
            #completed paren string
            if numOpen == numClosed == n:
               allParens.append( parenStr )
               return

            # otherwise, choose to add open brakcet here
            if numOpen < n:
               dfs(parenStr + "(", numOpen + 1, numClosed)

            #add a closed bracket if numOpen > numClosed
            if numOpen > numClosed and numClosed < n:
               dfs(parenStr + ")", numOpen, numClosed + 1) 
        
        dfs("", 0, 0)
        return allParens

    