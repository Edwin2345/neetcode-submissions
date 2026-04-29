/*
QQ
1. so the board down need to be filled for it to be valid, as logn as we dont duplicate its fine?
2. fixed board size?


Plan
1. seperate functions to check rows, columns, squares
2. use a set in each function to check for duplicates

Time Complexity
Space O(n) -> at most 9 in a map * 9 regions * 3 (1 for row,col,squar)
Time O(n) -> check all 81 squares at most 81*3 times

*/

func isValidRows(board [][]byte) bool {
    for r := 0; r < 9; r++ {
        rowSet := make(map[byte]bool)
        for c := 0; c < 9; c++ {
            if board[r][c] == '.' {
                continue
            }
            if rowSet[board[r][c]] {
                return false
            }
            rowSet[board[r][c]] = true
        }
    }
    return true
}

func isValidCols(board [][]byte) bool {
    for c := 0; c < 9; c++ {
        colSet := make(map[byte]bool)
        for r := 0; r < 9; r++ {
            if board[r][c] == '.' {
                continue
            }
            if colSet[board[r][c]] {
                return false
            }
            colSet[board[r][c]] = true
        }
    }
    return true
}

func isValidSquares(board [][]byte) bool {
   //check for duplicates inside square
   checkSquareDuplicates := func(rightCornerRow, rightCornerCol int) bool{
	    squareSet := make(map[byte]bool)
        for r := rightCornerRow; r <= rightCornerRow+2; r++ {
            for c := rightCornerCol; c <= rightCornerCol+2; c++ {
                if board[r][c] == '.' {
                    continue
                }
                if squareSet[board[r][c]] {
                        return false
                }
                squareSet[board[r][c]] = true
            }
		}
		return true
   }	

   //iterate though all right corners
   for rightCornerRow := 0; rightCornerRow <= 6; rightCornerRow += 3 {
        for rightCornerCol := 0; rightCornerCol <= 6; rightCornerCol += 3 {			
			if !checkSquareDuplicates(rightCornerRow, rightCornerCol){
				return false
			}
        }
    }
   return true
}


func isValidSudoku(board [][]byte) bool {
     return isValidRows(board) && isValidCols(board) && isValidSquares(board)
}
