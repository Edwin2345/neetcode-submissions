public class Solution {
    public int FindDuplicate(int[] nums) {
        //Equivalent to saying finding the haed of cycle 
        //as one value has two value (indexs) pointing to this (Creating cycle)
        int fastPtr=0;
        int slowPtr=0;
        while(true){
            fastPtr = nums[nums[fastPtr]];
            slowPtr = nums[slowPtr];
            if(fastPtr == slowPtr){
                break;
            }
        }

        int slowPtr2=0;
        while( slowPtr != slowPtr2 ){
            slowPtr2 = nums[slowPtr2];
            slowPtr = nums[slowPtr];
        }
        return slowPtr2;
    }
}
