class Solution:
#brute force: iterate through all squares and run bfs/dfs O( (RC)^2 )
# can reach the pacific if row < 0 (top) or col < 0 , reach atlantic if row >= num_row or col > num_col

#better, run bfs sarting with all squares immediately reachable by pacific -> store in pacific reahcbale set. Then do the same thing with altantic, any overlap is stored
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #create variables for bfs
        pacificQ, atlanticQ = deque(), deque()
        pacificSet, atlanticSet  = set(), set()
        NUM_ROWS, NUM_COLS, DIRECTIONS = len(heights), len(heights[0]), [[1,0], [-1,0], [0,1], [0,-1]]
        pacificAtlanticSquares = []

        #add all squares immediately reachable by pacific and atlantic
        for i in range(NUM_COLS):
            pacificQ.append( (0,i) )
            pacificSet.add( (0,i)  )
            atlanticQ.append( (NUM_ROWS-1,i) )
            atlanticSet.add( (NUM_ROWS-1,i) )
        for i in range(NUM_ROWS):
            pacificQ.append( (i,0) )
            pacificSet.add( (i,0) )
            atlanticQ.append( (i,NUM_COLS-1) )
            atlanticSet.add( (i,NUM_COLS-1) )
        
        def bfs(q, visitSet):
            while len(q) > 0:
                r,c = q.popleft()      
                #visit its neighbors if they are lower or equal
                for dr,dc in DIRECTIONS:
                    nr,nc = r+dr,c+dc
                    if min(nr,nc) < 0 or nr >= NUM_ROWS or nc >= NUM_COLS:
                       continue
                    #new square must be lower than current as water must flow away from it to the ocean
                    if heights[nr][nc] < heights[r][c] or (nr,nc) in visitSet:
                       continue
                    q.append( (nr,nc) )
                    visitSet.add( (nr,nc) )                     
        
        #run bfs on pacific, then atlatic, then compute overlap
        bfs(pacificQ, pacificSet)
        bfs(atlanticQ, atlanticSet)
        return  list( pacificSet.intersection(atlanticSet) )
        
    

        