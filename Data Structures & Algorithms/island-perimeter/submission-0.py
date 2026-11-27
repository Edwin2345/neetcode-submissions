class Solution:
    #1 island, no lakes
    #find a starting land piece and do dfs, but every dfs to
    #a non land is added permineter
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r,c):
            #non land square, increment perimeter and return
            if min(r,c) < 0 or r >= NUM_ROWS or c >= NUM_COLS or grid[r][c] == 0:
               return 1
            
            #otherwise, dfs to get the full perimeter
            curPerimeter = 0
            visited.add((r,c))

            for dr,dc in DIRECTIONS:
                nr,nc = r+dr, c+dc
                if (nr,nc) not in visited:
                   curPerimeter += dfs(nr,nc)

            return curPerimeter 
        
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if grid[r][c] == 1:
                   return dfs(r,c)                     


             
        