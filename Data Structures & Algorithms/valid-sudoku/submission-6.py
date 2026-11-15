class Solution:
    # solution, use maps of rowNum, colNum, squareNum to sets to see if duplicate numbers exist
    # "." should be skipped as represents blank field
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # map rows, cols, squares to the nums they contian
        rowMap, colMap, squareMap = defaultdict(set), defaultdict(set), defaultdict(set)

        for R in range(len(board)):
            for C in range(len(board[0])):
                # skip empty squares
                if board[R][C] == ".":
                    continue
                # duplciate found in row or column
                if board[R][C] in rowMap[R] or board[R][C] in colMap[C]:
                    return False
                # duplicate found in square
                if board[R][C] in squareMap[(R // 3, C // 3)]:
                    return False

                # save this number in all maps
                rowMap[R].add(board[R][C])
                colMap[C].add(board[R][C])
                squareMap[(R // 3, C // 3)].add(board[R][C])

        return True
