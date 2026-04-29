class Solution {
    public boolean isAnagram(String s, String t) {
          HashMap<Character, Integer> s_freq  = new  HashMap<Character, Integer>();

          //Freq Map String S
          for(int i=0; i<s.length(); ++i){
             char c = s.charAt(i);
             if( s_freq.get(c) == null ){
                 s_freq.put(c, 1);
             }
             else{
               s_freq.put(c, s_freq.get(c)+1);
             }
          }

          //Remove when checking t
          for(int j=0; j<t.length(); ++j){
             char c = t.charAt(j);

             if(s_freq.get(c) == null){
                return false;
             }
             else if(s_freq.get(c) == 1){
                s_freq.remove(c);
             }
             else{
                s_freq.put(c, s_freq.get(c)-1);
             }
          }
         

         return s_freq.size() == 0;
    }
}
