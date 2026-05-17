class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        toVisit = set()
        queue = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        #add starting node
        queue.append((0,0))
        toVisit.add((0,0))
        length = 0

        #use parent dictionary to map parent node to child to acutally print shortest path
        parent = {}
        parent[(0,0)] = None   
        finalPath = []   

        while len(queue):
            for _ in range(len(queue)):
               #process node -> check if we completed
               r,c = queue.popleft()
               if r == ROWS-1 and c == COLS-1:
                  cur = (r,c)
                  while cur is not None:
                     finalPath.append(cur)
                     cur = parent[cur]
                  finalPath.reverse()
                  print(finalPath)
                  return length
               
               #search neigbor cells if valid
               for dr, dc in directions:
                     nr, nc = r + dr, c + dc
                     if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS:
                        continue
                     if grid[nr][nc] == 1 or (nr,nc) in toVisit:
                        continue
                     
                     queue.append((nr,nc))            
                     toVisit.add((nr, nc))
                     parent[(nr,nc)] = (r,c)
            
            length += 1

        
        return -1