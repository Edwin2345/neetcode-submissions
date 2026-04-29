class Solution {
    public int findDuplicate(int[] nums) {
        HashMap<Integer, Integer> seenBefore = new HashMap<Integer, Integer>();

        for(int i=0; i<nums.length; ++i){
            if(seenBefore.get(nums[i]) != null){
                return nums[i];
            }

            seenBefore.put(nums[i], nums[i]);
        }
        return -1;
    }
}
