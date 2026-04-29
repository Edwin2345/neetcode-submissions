class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        queue = deque()   
        visit = set()    
        ROWS,COLS = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        #add all inital rotting frut to queue and count fresh oranges
        freshCount = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCount += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
                    visit.add((r,c))
        
        #perform bfs until queue empty -> each level if
        while len(queue) > 0 and freshCount > 0:
            #process level by level
            for i in range(len(queue)):
                r,c = queue.popleft()

                #set all adjacent oranges as rotten
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    #oob or seen before
                    if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or (nr,nc) in visit:
                        continue
                    if grid[nr][nc] == 1:
                       grid[nr][nc] = 2
                       freshCount -= 1
                       queue.append((nr,nc))
                       visit.add((nr,nc))
            
            #each stage is a new minute
            minutes += 1
        
      
        #return total time to rot all
        return minutes if freshCount == 0 else -1
                


            