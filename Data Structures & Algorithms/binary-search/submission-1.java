class Solution {
    public int search(int[] nums, int target) {
        return searchRec(nums, target, 0, nums.length-1);
    }


    public int searchRec(int[] nums, int target, int low, int high){
        if(low > high)
        {
           return -1;
        }
        else{
           int mid = low + (high-low)/2;
           if(nums[mid] == target){
              return mid;
           }
           else if(nums[mid] > target){
              return searchRec(nums, target, low, mid-1);
           }
           else{
              return searchRec(nums, target, mid+1, high);
           }
        }
    }
}
