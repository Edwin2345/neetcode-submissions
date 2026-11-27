class Solution:
    # 1 island, no lakes
    # find a starting land piece and do dfs, but every dfs to
    # a non land is added permineter
    # TC: O(RC) SC: O(RC) as traversr and store entire grid
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(sr,sc):
            # initilze first land node
            q = deque([(sr,sc)])
            visit = set([(sr,sc)])
            perimeter = 0

            while len(q) > 0:
                #pop the land cell
                r,c = q.popleft()

                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    #check adjacent if they are non water -> adds to perimeter
                    if min(nr,nc) < 0 or nr >= NUM_ROWS or nc >= NUM_COLS or grid[nr][nc] == 0:
                       perimeter += 1
                       continue
                    #if land mark as visit and add to queur
                    if (nr,nc) not in visit:
                       q.append( (nr,nc) )
                       visit.add( (nr,nc) )  

            return perimeter

        # find first land sqaure to bfs from - as only 1 island
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if grid[r][c] == 1:
                    return bfs(r,c)
