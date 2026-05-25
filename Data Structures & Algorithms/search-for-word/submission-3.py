class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        wordArr = []

        def dfs(r, c):
            #edge cases
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
               return False
            elif (r,c) in visited or board[r][c] != word[len(wordArr)]: 
               return False

            #add correct word cell and see if it matches
            wordArr.append(board[r][c])
            visited.add( (r,c) )
            if len(wordArr) == len(word):
               return True
            
            #dfs to remaining squares to see if match found
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if dfs(nr,nc):
                   return True
            
            #backtrack
            wordArr.pop()
            visited.remove( (r,c) )   
            return False                   
         
        #loop through board, find cells that match starting eltter
        for r in range(ROWS):
            for c in range(COLS):
                visited.clear()
                if board[r][c] == word[0] and dfs(r,c):
                   return True
         
        return False
            

            
            
        