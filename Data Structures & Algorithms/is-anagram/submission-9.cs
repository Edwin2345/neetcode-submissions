public class Solution {
    public bool IsAnagram(string s, string t) {
       if(s.Length != t.Length){
         return false;
       }

       //iterate through both
       Dictionary<char, int> freqCnt = new Dictionary<char, int>();
       foreach(char sc in s){
          if(!freqCnt.ContainsKey(sc)){
            freqCnt[sc] = 1;
          }
          else{
            freqCnt[sc] += 1;
          }
       }

       foreach(char tc in t){
          if(!freqCnt.ContainsKey(tc)){
            return false;
          }
          else if(freqCnt[tc] == 1){
             freqCnt.Remove(tc);
          }
          else{
             freqCnt[tc] -= 1;
          }
       }


       return freqCnt.Count == 0;
    }
}
