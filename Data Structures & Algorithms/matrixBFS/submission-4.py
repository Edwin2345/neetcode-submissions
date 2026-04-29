class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        #set all bfs variables
        queue = deque()
        queue.append((0,0))
        visit = set()
        ROWS,COLS = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        #check if path from start to end is even possible
        if grid[0][0] or grid[ROWS-1][COLS-1]:
            return -1
        
        #LENGTH is Number of Moves
        length = 0
        while len(queue) > 0:
            stageSize = len(queue)
            for i in range(stageSize):
                #process curr coordinates -> check if found valid path
                r,c = queue.popleft()
                if r == ROWS-1 and c == COLS-1 and grid[r][c] == 0:
                    return length

                #add all other directions if valid
                for dr,dc in directions:
                    nr,nc = r + dr, c + dc
                    #invalid egde cases
                    if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    if grid[nr][nc] == 1 or (nr,nc) in visit:
                        continue
                    
                    queue.append((nr,nc))
                    visit.add((nr,nc))

            #each new stage is additional length in apth
            length += 1

        #no path found
        return -1