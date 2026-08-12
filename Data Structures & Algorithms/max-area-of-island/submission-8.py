class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        NUM_ROWS, NUM_COLS, DIRECTIONS = len(grid), len(grid[0]), [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        visit = set()
        q = deque()

        def bfs(r, c):
            #initalize queue with current sqaure
            q.append( (r,c) )
            visit.add( (r,c) )
            islandArea = 0

            while len(q) > 0:
                #add current square to island area
                r,c = q.popleft()
                islandArea += 1

                #add valid neighboring land sqaures apart of the island
                for dr,dc in DIRECTIONS:
                    nr,nc = r + dr, c + dc
                    if min(nr,nc) < 0 or nr >= NUM_ROWS or nc >= NUM_COLS:
                        continue
                    if grid[nr][nc] == 0 or (nr,nc) in visit:
                        continue

                    q.append( (nr,nc) )
                    visit.add( (nr,nc) )   
                  
            return islandArea
        
        #check all unvisted land squares, and fully bfs to get island size
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                   islandArea = bfs(r,c)
                   maxArea = max(maxArea, islandArea) 

        return maxArea
