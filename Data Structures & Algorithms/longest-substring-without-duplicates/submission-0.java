class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> windowSet = new HashSet<Character>();

        int L=0;
        int maxLength=0;

        for(int R=0; R<s.length(); ++R){
            //add to set if can
            if( !windowSet.contains(s.charAt(R)) ){
                windowSet.add(s.charAt(R));
            }
            else{
                 //remove and shift window until can add new character
                 while( windowSet.contains(s.charAt(R)) ){
                    windowSet.remove(s.charAt(L));
                    ++L;
                 }    
                 windowSet.add(s.charAt(R));           
            }

            //calculate length for every new char and see if its new max
            if(maxLength < R-L+1){
               maxLength = R-L+1;
            }
        }

        return maxLength;
    }
}
