class Solution:
    # 4 directions,can't use same square more than once
    #word is not "", board has at least 1 square

    #TC: O(R*C*4^L) where R,C are num of rows and cols, and L is lenght of word
    #   at worst for every squar eoyu chek 4fdirecitosn for a path of size L

    #SC: O(L) for set and call stack
    def exist(self, board: List[List[str]], word: str) -> bool:

        NUM_ROWS, NUM_COLS = len(board), len(board[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(r, c, i):
            # board index out of bounds
            if min(r, c) < 0 or r >= NUM_ROWS or c >= NUM_COLS:
                return False
            # square already used or doesnt match target index
            if (r, c) in visited or board[r][c] != word[i]:
                return False

            # succesfully found the enitre word
            if i == len(word) - 1:
                return True

            # otherwise, mark as visited and search for next letter in all 4 direcitons
            visited.add( (r,c) )
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    return True

            # couldn't find match form this square onwards
            visited.remove( (r,c) )
            return False

        # check every sqaure as startign point for word
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                visited.clear()
                if dfs(r, c, 0):
                    return True

        return False
