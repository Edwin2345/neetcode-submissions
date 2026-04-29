class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        queue.append((0,0))
        visit = set()
        ROWS,COLS = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]

        pathLength = 1
        while len(queue) > 0:
            stageLength = len(queue)

            for i in range(stageLength):
                #process cur node
                r,c = queue.popleft()
                if r == ROWS-1 and c == COLS-1 and grid[r][c] == 0:
                    return pathLength                
                
                #add all valid child directional nodes
                for dr,dc in directions:
                    nr,nc = r + dr, c + dc
                    if min(r,c) < 0 or r >= ROWS or c >= COLS:
                       continue
                    if grid[r][c] == 1 or (r,c) in visit:
                       continue
                    queue.append((nr,nc))
                
                visit.add((r,c))
            
            pathLength += 1
                    
        #no path found
        return -1