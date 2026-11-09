class Solution:
  #longest ss with only one character, inclduign replacements
  #slide widnow over substring countign character freq: number_rep = (ssLen - max(freq))
  #O(N) TC single scan,  O(m) space for frequency map where m is number of unique character
    def characterReplacement(self, s: str, k: int) -> int:
        letterFreq = defaultdict(int)
        L = 0
        maxSSLen = 0
        for R in range(len(s)):
          #add current letter
            letterFreq[s[R]] += 1
            
            #if we need to replace too many chaarcters
            #shrink substrign from left till valid substring
            while R-L+1 - max(letterFreq.values()) > k:
                letterFreq[s[L]] -= 1
                L += 1
            
            #update max length
            maxSSLen = max(maxSSLen, R-L+1)
        
        return maxSSLen
        