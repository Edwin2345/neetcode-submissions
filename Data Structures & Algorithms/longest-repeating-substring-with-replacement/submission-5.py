class Solution:
  #longest ss with only one character, inclduign replacements
  #slide widnow over substring countign character freq: number_rep = (ssLen - max(freq))
    def characterReplacement(self, s: str, k: int) -> int:
        letterFreq = {}
        L = 0
        maxSSLen = 0
        for R in range(len(s)):
          #add current letter
            if s[R] not in letterFreq:
               letterFreq[s[R]] = 1
            else:
               letterFreq[s[R]] += 1
            
            #if we need to replace too many chaarcters
            #shrink substrign from left till valid substring
            while R-L+1 - max(letterFreq.values()) > k:
                letterFreq[s[L]] -= 1
                L += 1
            
            #update max length
            maxSSLen = max(maxSSLen, R-L+1)
        
        return maxSSLen
        