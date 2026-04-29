class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t){
       if(s.length != t.length){
         return false;
       }

       const sMap = new Map();
       const tMap = new Map();

       for(let i=0; i<s.length; ++i){
           if(!sMap.has(s[i])){
              sMap.set(s[i],1);
           }
           else{
              sMap.set(s[i], sMap.get(s[i]) + 1);
           }
           if(!tMap.has(t[i])){
              tMap.set(t[i],1);
           }
           else{
              tMap.set(t[i], tMap.get(t[i]) + 1);
           }      
       }

       //check if counts are sam
       for(let k of sMap.keys()){
          if(!tMap.has(k) || tMap.get(k) != sMap.get(k)){
             return false;
          }
       }

       return true;
    }
}
