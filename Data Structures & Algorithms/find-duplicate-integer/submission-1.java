class Solution {
    public int findDuplicate(int[] nums) {
      // would only get if seen before -> secretly head of cycle (duplicate number have 2 index pointng to it)
      
      //find cycle point
      int fastPtr=0;
      int slowPtr=0;

      while(true){
        fastPtr = nums[nums[fastPtr]];
        slowPtr = nums[slowPtr];

        if(fastPtr == slowPtr){
            break;
        }
      }

      //Find start of cycle
      int slowPtr2 = 0;
      while(slowPtr2 != slowPtr){
         slowPtr2 = nums[slowPtr2];
         slowPtr = nums[slowPtr];
      }
       
       return slowPtr;
    }
}
