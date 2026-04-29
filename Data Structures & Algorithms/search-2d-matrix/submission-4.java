class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rowMAX =  matrix.length-1;
        int colMAX =  matrix[0].length-1;

        //binary search the rows
        int r_top=0;
        int r_bot=rowMAX;
        while(r_top <= r_bot){
            int r_mid = r_top + (r_bot-r_top)/2;
            // too large -> search higher row
            if( matrix[r_mid][colMAX] < target ){               
               r_top = r_mid+1;
            }
            // too small -> search low row
            else if( matrix[r_mid][0] > target ){
              r_bot = r_mid-1;
            }
            else{
               break;
            }
        }

        if(r_top > r_bot){
            return false;
        }

        //binary search the columns of the rows
        int ROW = r_top + (r_bot-r_top)/2;
        int c_low = 0;
        int c_high = colMAX;
        while( c_low <= c_high){
            int c_mid = c_low + (c_high-c_low)/2;
            if(matrix[ROW][c_mid] == target){
              return true;
            }
            else if(matrix[ROW][c_mid] > target){
                c_high = c_mid-1;
            }
            else{
                c_low = c_mid+1;
            }
        }

        return false;
    }
}
