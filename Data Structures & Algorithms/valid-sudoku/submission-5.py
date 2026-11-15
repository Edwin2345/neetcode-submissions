class Solution:
    # break up into functions to check rows, cols,a nd sqaures for duplicates
    #TC: O(n^2) time, O(n) space
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #let n be the deminion of the squr matric (in this 9)
        ROW_NUM, COL_NUM = 9, 9
     
        #O(n^2) time, O(n) space
        def areColumnsValid():
            for C in range(COL_NUM):
                colSet = set()
                for R in range(ROW_NUM):
                    if board[R][C] == ".":
                       continue
                    if board[R][C] in colSet:
                        return False
                    colSet.add(board[R][C])
            return True

        #O(n^2) time, O(n) space
        def areRowsValid():
            for R in range(ROW_NUM):
                rowSet = set()
                for C in range(COL_NUM):
                    if board[R][C] == ".":
                       continue
                    if board[R][C] in rowSet:
                        return False
                    rowSet.add(board[R][C])
            return True

        #O(n^2) time, O(n) space
        def checkSquare(startR, startC):
            squareSet = set()
            for R in range(startR, startR + 3):
                for C in range(startC, startC + 3):
                    if board[R][C] == ".":
                       continue
                    if board[R][C] in squareSet:
                        return False
                    squareSet.add(board[R][C])
            return True

        def areSquaresValid():
            for R in range(0, 7, 3):
                for C in range(0, 7, 3):
                    if not checkSquare(R, C):
                        return False
            return True

        return areRowsValid() and areColumnsValid() and areSquaresValid()
