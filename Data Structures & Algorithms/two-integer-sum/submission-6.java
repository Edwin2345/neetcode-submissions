class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> seenBefore = new  HashMap<Integer,Integer>();

        for(int i=0; i<nums.length; ++i){
            if(seenBefore.get(target-nums[i]) != null){
              return new int[]{seenBefore.get(target-nums[i]), i};
            }
            seenBefore.put(nums[i], i);
        }

        return new int[]{-1,-1};
    }
}
