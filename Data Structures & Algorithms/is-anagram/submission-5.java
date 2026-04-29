class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character,  Integer> counter_s = new HashMap<Character,Integer>();
        HashMap<Character, Integer> counter_t = new HashMap<Character,Integer>();

        for(int i=0; i<s.length(); ++i){
           counter_s.put( s.charAt(i), 1 + (counter_s.get(s.charAt(i)) == null ?  0 : counter_s.get(s.charAt(i))) );
           counter_t.put( t.charAt(i), 1 + (counter_t.get(t.charAt(i)) == null ?  0 : counter_t.get(t.charAt(i))) );
        }

        for(Character letter : counter_s.keySet()){
            if( counter_t.get(letter) != counter_s.get(letter)){
                return false;
            }
        }

        return true;

    }
}
