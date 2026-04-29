class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:        

        #bfs to find closet treasure chest
        INF = 2**31-1
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS,COLS = len(grid),len(grid[0])

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visit = set()            
            visit.add((r,c))
            dist = 0

            while queue:                
                for i in range(len(queue)):
                    #process cur not -> found treasure path
                    r,c = queue.popleft()
                    if grid[r][c] == 0:
                        return dist
                    
                    #add all other adjacent land cells to queue
                    for dr,dc in directions:
                        nr,nc = r+dr,c+dc
                        #edge case --> oob
                        if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS:
                            continue
                        #edge case --> already visited or not water
                        if grid[nr][nc] == -1 or (nr,nc) in visit:
                            continue
                        queue.append((nr,nc))
                        visit.add((nr,nc))

                dist += 1
                                  
            #no path found
            return INF
        
        #iterate through grid and update all landcells      
        for r in range(ROWS):
            for c in range(COLS):                
                if grid[r][c] == INF:
                   grid[r][c] = bfs(r,c)