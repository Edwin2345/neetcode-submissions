class Solution:
    # can we make assumption that numebr of treasure chests is much less than nhmber of islands
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit, q = set(), deque()
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        NUM_ROWS, NUM_COLS, INF = len(grid), len(grid[0]), 2**31 - 1

        # add all the tresure chests to the queue
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        # bfs
        dist = 0
        while len(q) > 0:
            # update land level by level
            for _ in range(len(q)):
                # pop grid from queue -> if its a land cell update its min distance to a island
                r, c = q.popleft()
                if grid[r][c] > 0 and dist < grid[r][c]:
                    grid[r][c] = dist

                # add it neighboring land
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr >= NUM_ROWS or nc >= NUM_COLS:
                        continue
                    if grid[nr][nc] <= 0 or (nr, nc) in visit:
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))

            #increment the distance from tresure chests
            dist += 1
