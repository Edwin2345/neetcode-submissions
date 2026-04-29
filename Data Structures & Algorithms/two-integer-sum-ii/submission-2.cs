public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int L=0;
        int R=numbers.Length-1;

        while(L<R){
           int sum = numbers[L] + numbers[R];
           if(sum == target){
             return new int[]{L+1,R+1};
           }
           else if(sum < target){
             ++L;
           }
           else{
             --R;
           }
        }

        //none found
        return new int[]{-1, -1};
    }
}
