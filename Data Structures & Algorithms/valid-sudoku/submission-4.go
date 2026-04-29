/*

Optimal solution -> 1 pass

- or use one map and strign concat to differentiate betrween rows,cols, squares
- do "4 in row 1" for example

*/

func isValidSudoku(board [][]byte) bool {

    regions := make(map[string]bool,0)

    for r := 0; r<9; r++{
        for c := 0; c<9; c++{
            //skip empty square
            if board[r][c] == '.'{
                continue
            }
            
            colKey := fmt.Sprintf("%s in col %d", board[r][c], c)
            rowKey := fmt.Sprintf("%s in row %d", board[r][c], r)
            squareKey := fmt.Sprintf("%s in square %d-%d", board[r][c], r/3, c/3)
 
            //check if duplicate detected, else add to set
            if regions[colKey] || regions[rowKey] || regions[squareKey]{
                return false
            }
            regions[colKey] = true
            regions[rowKey] = true
            regions[squareKey] = true
        }
    }

    return true
}
