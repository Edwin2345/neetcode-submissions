class Solution:
    #approach, iterate throguh grid, if square is land is not visited, new island
    #then run dfs or bfs to fully explore ispland, adding to visited
    #Time: O(NUM_ROWS*NUM_COLS) as me mostly vist eahc seuare ones
    #Space; O((NUM_ROWS*NUM_COLS) for visited set
    def numIslands(self, grid: List[List[str]]) -> int:
        NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()

        def dfs(r,c):
            if min(r,c) < 0 or r >= NUM_ROWS or c >= NUM_COLS:
               return
            if grid[r][c] == "0" or (r,c) in visited:
               return 
            #mark square as visited to inbdicate part of current island (not double counted)
            visited.add((r,c))
            for dr,dc in DIRECTIONS:
                dfs(r + dr, c + dc)
                
        numIslands = 0
        for r in range(NUM_ROWS):
           for c in range(NUM_COLS):
               if grid[r][c] == "1" and (r,c) not in visited:
                  numIslands += 1
                  dfs(r,c)
        
        return numIslands
               
        