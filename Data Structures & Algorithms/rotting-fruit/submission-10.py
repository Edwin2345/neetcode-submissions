class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        queue = deque()
        minutes = 0
        toVisit = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]        
        
        #get a count of the total numebr of fresh fruit
        # and add all rotten fruit as starting point
        numFreshFruit = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                   numFreshFruit += 1
                elif grid[r][c] == 2:
                   queue.append((r,c))
                   toVisit.add((r,c))    
        
        #easy case: no fresh fruit to rot:
        if numFreshFruit == 0:
           return 0 

        #bfs this bitch
        while len(queue):
            for _ in range(len(queue)):
                #process current node
                r,c = queue.popleft()
                if grid[r][c] == 1:
                   numFreshFruit -= 1 
                   grid[r][c] = 2
                if numFreshFruit == 0:
                   return minutes

                #add valid fresh children to be processd 
                for dr, dc in directions:
                    nr,nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS:
                       continue
                    if grid[nr][nc] != 1 or (nr,nc) in toVisit:
                       continue
                    
                    queue.append((nr,nc))
                    toVisit.add((nr,nc))

            #increamte minute count after each level
            minutes += 1  
        
        #fresh fruit not all rotten
        return -1

