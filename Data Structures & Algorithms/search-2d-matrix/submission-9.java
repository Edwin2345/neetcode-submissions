class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        //int[][] matrix = new int[4][5];
        //int[][] matrix = new int{{1,2,3}, {4,5,6}}
        int m = matrix.length;
        int n = matrix[0].length;

        int low=0;
        int high=m*n-1;

        while(low <= high){
            int mid = low + (high-low)/2;
            int r = mid / n;
            int c = mid % n;

            if(matrix[r][c] == target){
                return true;
            }
            else if(matrix[r][c] < target){
                low = mid + 1;
            }
            else{
                high = mid-1;
            }
        }

        return false;
        
    }
}
