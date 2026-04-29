class Solution {
    public boolean isPalindrome(String s) {
        String cstr = s.replaceAll("[^A-Za-z0-9]","");
        int i=0;
        int j=cstr.length()-1;

        while(i<j){
            if(Character.toLowerCase(cstr.charAt(i)) != Character.toLowerCase(cstr.charAt(j))){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
