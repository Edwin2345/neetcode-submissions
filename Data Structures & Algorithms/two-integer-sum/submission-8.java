class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> seenBefore = new HashMap<Integer,Integer>();

        for(int i=0; i<nums.length-1; ++i){
           for(int j=i+1; j<nums.length; ++j){
                if(nums[j] == target-nums[i]){
                   return new int[]{i,j};
                }
           }
        }

        return new int[]{-1,-1};
    }
}
