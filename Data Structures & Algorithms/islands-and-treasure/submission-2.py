class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS = len(grid), len(grid[0])
        queue = deque()
        toVisit = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        distance = 0

        #add all treasure chest to traverse
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                   queue.append((r,c))
                   toVisit.add((r,c))


        #bfs level by level, updating all land cells (>0)
        while len(queue): 
            for _ in range(len(queue)):
                #update land squares distance to treaure
                r,c  = queue.popleft()
                if grid[r][c] > 0:
                    grid[r][c] = min(grid[r][c], distance)
                  
                #add other unexplored land cells to traverse
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    if grid[nr][nc] <= 0 or (nr,nc) in toVisit:
                        continue                        
                    queue.append((nr,nc))
                    toVisit.add((nr,nc))

            #increase search distance from treasure
            distance += 1          
              
