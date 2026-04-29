class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> prevSeen = new HashMap<Integer, Integer>();
        int[] ans = new int[2];

        for(int i=0; i<nums.length; ++i){
            if(prevSeen.get(target-nums[i]) != null){
                ans[0] = prevSeen.get(target-nums[i]);
                ans[1] = i;
                return ans;
            }
            prevSeen.put(nums[i],i);
        }

        return new int[]{};
    }
}
