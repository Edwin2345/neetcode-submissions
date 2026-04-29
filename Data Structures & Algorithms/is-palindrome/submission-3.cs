public class Solution {
    public bool IsPalindrome(string s) {
        int L=0;
        int R=s.Length-1;

        //While Loop Condition Chekced Before Body BEgins and After Body Finishes

        while(L<R){
            //skip until find a char thats  alpha numeric
            while( L<R && !char.IsLetterOrDigit(s[L])){
               ++L;
            }
            while(L<R && !char.IsLetterOrDigit(s[R])){
               --R;
            }

            //check if palindrone
            if(char.ToUpperInvariant(s[L]) != char.ToUpperInvariant(s[R])){
                return false;
            }

            //go to next L,R positon
            ++L;
            --R;
        }
        return true;
    }
}
