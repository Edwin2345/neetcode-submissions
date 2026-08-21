class Solution:
   #Multisoruce bfs: add all rotten fruit to queue, but also coutn fresh fruit
   #run bfs where dist is minutes elasped, process byd ecrmenitng if fresh fruit only
   # if numFreshFruit == 0 return min else -1
   #time and space is O(R*C)
    def orangesRotting(self, grid: List[List[int]]) -> int:
         NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
         DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
         q, visit = deque(), set()

        #add all rotting fruit + coutn fresh fruit
         freshFruitCount = 0
         for r in range(NUM_ROWS):
           for c in range(NUM_COLS):
               if grid[r][c] == 2:
                  q.append( (r,c) )
                  visit.add( (r,c) )
               elif grid[r][c] == 1:
                  freshFruitCount += 1
         
         #edge case: no fruti to rot
         if freshFruitCount == 0:
            return 0

         minutes = 0
         while len(q) > 0:
            for _ in range(len(q)):
               #foudn fresh fruit -> decremnt fresh count and see if
               r,c = q.popleft()
               if grid[r][c] == 1:
                  freshFruitCount -= 1
                  if freshFruitCount == 0:
                     return minutes
               
               #add its fresh children to rot next minut
               for dr,dc in DIRECTIONS:
                  nr,nc = r+dr, c+dc
                  if min(nr,nc) < 0 or nr >= NUM_ROWS or nc >= NUM_COLS:
                     continue
                  if (nr,nc) in visit or grid[nr][nc] != 1:
                     continue
                  q.append( (nr,nc) )
                  visit.add( (nr,nc) )
            #incremnt minutes every level      
            minutes += 1
        
         #cant rot all fruit
         return -1
      
        