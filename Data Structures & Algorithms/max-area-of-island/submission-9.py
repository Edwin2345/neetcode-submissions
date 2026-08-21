class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:   
        NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
        visit = set()
        q = deque()
        maxArea = 0

        def bfs(r,c):
            q.append((r,c))
            visit.add((r,c))
            area = 0 
            while len(q) > 0:
                #add current land sqaure to islands area
                r,c = q.popleft()
                area += 1
                #add neightboring unexplored land to queue
                for dr,dc in DIRECTIONS:
                    nr,nc = r + dr, c + dc
                    if min(nr,nc) < 0 or nr >= NUM_ROWS or nc >= NUM_COLS:
                       continue 
                    if grid[nr][nc] == 0  or (nr,nc) in visit:
                       continue
                    q.append((nr,nc))
                    visit.add((nr,nc)) 

            return area

        #Traverse throguh all grid positions
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                #new island found -> measure its area
                if grid[r][c] == 1 and (r,c) not in visit:
                   maxArea = max(maxArea, bfs(r,c)) 


        return maxArea

