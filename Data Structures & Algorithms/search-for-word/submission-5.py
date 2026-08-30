class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        NUM_ROWS, NUM_COLS = len(board), len(board[0])
        DIRECTIONS = [[1,0],[-1,0], [0,1], [0,-1]]
        visited = set()

        def dfs(r,c):
            #add current valid character to path -> check if word found              
            visited.add( (r,c) )
            if len(visited) == len(word):
               return True

            #otherwise explroe children if they match the required letter
            for dr,dc in DIRECTIONS:
                nr,nc = r+dr,c+dc
                if min(nr,nc) < 0 or nr >= NUM_ROWS or nc >= NUM_COLS:
                   continue
                if (nr,nc) in visited or board[nr][nc] != word[len(visited)]:
                   continue
                if dfs(nr,nc):
                   return True 
                
            #backtrack and return false -> no word found there
            visited.remove( (r,c) )
            return False

        #find a valid starting character and dfs
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if board[r][c] == word[0] and dfs(r,c):
                   return True
        
        return False

        
