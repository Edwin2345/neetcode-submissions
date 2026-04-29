class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        queue = deque()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        maxArea = 0

        def bfs(r,c):
            area = 0
            queue.append((r,c))
            grid[r][c] = 0
            
            while len(queue) > 0:
                #add current square to area
                r,c = queue.popleft()
                area += 1

                #explore all other adjacent land squares
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    if grid[nr][nc] == 0:
                        continue
                    queue.append((nr,nc))
                    grid[nr][nc] = 0
            return area

        #iterate through grid and find max are of all new islands
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea,bfs(r,c))

        return maxArea

                


                    
