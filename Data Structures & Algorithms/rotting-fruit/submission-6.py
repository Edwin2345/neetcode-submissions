class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs solution
        ROWS,COLS = len(grid),len(grid[0])
        visit = [[0]*COLS for _ in range(ROWS)]
        print(visit)
        
        #count number of fresh bananas, and add all initally rotten to queue
        queue = deque()
        freshCount = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                   freshCount += 1
                elif grid[r][c] == 2:
                   queue.append((r,c))
                   visit[r][c] = 1
        
        #BFS 
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        minute = 0
        while freshCount > 0 and len(queue) > 0:
            #rot all fruit in current minute
            for i in range(len(queue)):
                #pop a rotton fruit
                r,c = queue.popleft()

                #infect fresh neighbors
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    #edge cases: oob, visited already, not fresh
                    if (
                    min(nr,nc) < 0 or nr >= ROWS or nc >= COLS 
                    or visit[nr][nc] or grid[nr][nc] != 1
                    ):
                      continue
                    #mark square as infected and add to queue  
                    grid[nr][nc] = 2
                    visit[nr][nc] = 1
                    freshCount -= 1
                    queue.append((nr,nc))                   
            
            #move onto next minute
            minute += 1
          
        #couldn't rot all fresh fruit
        return  minute if freshCount == 0 else -1
        

                      


