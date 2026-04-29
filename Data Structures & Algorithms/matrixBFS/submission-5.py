class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        queue = deque()
        visit = set()
        ROWS,COLS = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        #check if a valid path is even possible
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        

        #start at top and bfs -> each stage is the length of path
        queue.append((0,0))
        visit.add((0,0))
        length = 0
        while len(queue) > 0:
            
            for i in range(len(queue)):           
                r,c = queue.popleft()      
                if (r,c) == (ROWS-1,COLS-1):
                    return length          

                #explore adjacent
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc 
                    #oob or invalid
                    if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS:
                        continue 
                    if (nr,nc) in visit or grid[nr][nc] == 1:
                        continue
                    #add valid adjacent 
                    queue.append((nr,nc))
                    visit.add((nr,nc))
            
            #each stage is new path length
            length += 1
        
        #no valid path found
        return -1
                
