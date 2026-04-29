class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let L=0;
        let R=s.length-1;

        while(L<R){
           //go to alphanumeric character
           while(L<R && s[L].match(/^[0-9a-z]+$/i) == null){
              ++L;
           }
           while(L<R && s[R].match(/^[0-9a-z]+$/i) == null){
              --R;
           }

           if( s[L].toLowerCase() !== s[R].toLowerCase()){
              return false;
           }

           ++L;
           --R;
        }

        return true;
    }
}
