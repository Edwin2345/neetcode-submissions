class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
       #edge case: start or end is blocked off
       if grid[0][0] == 1 or grid[-1][-1] == 1:
          return -1 

       q, visit = deque(), set()
       NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
       DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]


       #add stating square
       q.append((0,0))
       visit.add((0,0))
       pathLen = 1

       #initalize parent dict to show shroest path
       parentDict = {(0,0) : None}

       while len(q) > 0:
           for _ in range(len(q)):
               #process current grid -> see if 
               r,c = q.popleft()
               if r == NUM_ROWS-1 and c == NUM_COLS-1:
                  #print shortest path and retunr its length
                  curCoords = (r,c)
                  path = []
                  while curCoords is not None:
                        path.append(curCoords)
                        curCoords = parentDict[curCoords]
                  path.reverse()
                  print("Shortest Path: ", path)
                  return pathLen
               
               #add reachable children
               for dr,dc in DIRECTIONS:
                   nr, nc =  r + dr, c + dc
                   if min(nr,nc) < 0 or nr >= NUM_ROWS or nc >= NUM_COLS:
                      continue
                   if grid[nr][nc] == 1 or (nr,nc) in visit:
                      continue
                    
                   q.append( (nr,nc) )
                   visit.add( (nr,nc) ) 
                   parentDict[(nr,nc)] = (r,c)
           
           #increease pathLen for each bfs layer 
           pathLen += 1
       
       #no path found
       return -1