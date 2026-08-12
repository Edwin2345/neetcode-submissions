class Solution:
    #approach, iterate throguh grid, if square is land is not visited, new island
    #then run dfs or bfs to fully explore ispland, adding to visited
    #Time: O(NUM_ROWS*NUM_COLS) as me mostly vist eahc seuare ones
    #Space; O((NUM_ROWS*NUM_COLS) for visited set
    def numIslands(self, grid: List[List[str]]) -> int:
        NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
        visit = set()
        q = deque()

        def bfs(r,c):
            #add starting square
            q.append( (r,c) )
            visit.add( (r,c) )

            while len(q) > 0:               
               r,c = q.popleft()
               # add children to be explored to visit entire island
               for dr, dc in DIRECTIONS:
                  nr,nc = r+dr, c+dc
                  if min(nr, nc) < 0 or nr >= NUM_ROWS or nc >= NUM_COLS:
                     continue
                  if grid[nr][nc] == "0" or (nr,nc) in visit:
                     continue
                  q.append( (nr,nc) )
                  visit.add( (nr,nc) )
                  
        numIslands = 0
        for r in range(NUM_ROWS):
           for c in range(NUM_COLS):
               if grid[r][c] == "1" and (r,c) not in visit:
                  numIslands += 1
                  bfs(r,c)
        
        return numIslands
               
        