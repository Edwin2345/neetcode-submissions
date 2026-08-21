class Solution:
    #iterate throguh grids, if you find an island, bfs from there
    #update land cells ( not -1 and not 0) if distance is smaller than curreent val;ue


    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()
        visit = set()
        dist = 0

      #add all treasures
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if grid[r][c] == 0:
                   q.append( (r,c) ) 
                   visit.add( (r,c) )

        while len(q) > 0:
            for _ in range(len(q)):
                #update the land squares distance to a treasure
                #only will traverse once
                r,c = q.popleft()
                grid[r][c] = dist

                #add traversable cells for the next level
                for dr,dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if min(nr,nc) < 0 or nr >= NUM_ROWS or nc >= NUM_COLS:
                       continue
                    if grid[nr][nc] == -1 or grid[nr][nc] == 0 or (nr,nc) in visit:
                       continue
                    q.append( (nr,nc) )
                    visit.add( (nr,nc) ) 
            #distance of path to treasure increases by one for each level
            dist += 1

        
        