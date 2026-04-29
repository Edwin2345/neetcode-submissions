class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rowMAX =  matrix.length;
        int colMAX =  matrix[0].length;

        int low = 0;
        int high = rowMAX*colMAX-1;
        while(low <= high){
            int mid = low + (high-low)/2;
            int row = mid / colMAX;
            int col = mid % colMAX;

            if(matrix[row][col] == target){
                return true;
            }
            else if(matrix[row][col] > target){
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }


        return false;
    }
}
