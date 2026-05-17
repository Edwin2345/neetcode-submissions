class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        toVisit = set()
        queue = deque()
        length = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        #add starting node
        queue.append((0,0))
        toVisit.add((0,0))

        while len(queue):
              for _ in range(len(queue)):
                  #process current node, check if we are at end
                  r,c = queue.popleft()                                     
                  if r == ROWS-1 and c == COLS-1:
                     return length

                  #add neighbors only if they are valid
                  for dr,dc in directions:
                      nr, nc = r + dr, c + dc                    
                      if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS:
                         continue
                      if grid[nr][nc] == 1 or (nr,nc) in toVisit:
                         continue

                      queue.append((nr,nc))
                      toVisit.add((nr,nc))
                                                      
              #path length increase by one for each level
              length += 1

        return -1