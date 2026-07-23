class Solution:
    #P: create frequency count map of both, and keep track of matches
    #P: slide a window with L and R pointers across s
    #P: keep a minLength and minL and minR to keep track of min window
    def minWindow(self, s: str, t: str) -> str:
        #edge case
        if len(s) < len(t):
           return "" 
        
        #build freq count of T
        freqT = {} 
        for c in t:
            if c not in freqT:
               freqT[c] = 1
            else:
               freqT[c] += 1  
        
        #sliding window
        minLength, minL, minR = float("inf"), -1, -1
        freqS = {}
        numMatches = 0
        L=0
        for R in range(len(s)):
            #add to window from the right
            if s[R] not in freqS:
               freqS[s[R]] = 1
            else:
               freqS[s[R]] += 1   

            #update number of matches         
            if s[R] in freqT and freqS[s[R]] == freqT[s[R]]:
               numMatches += 1 

            #found a valid subString
            while numMatches == len(freqT):
                #update min
                if minLength > R-L+1:
                   minLength = R-L+1 
                   minL, minR = L, R
                
                #shift left, updateing matches
                if s[L] in freqT and freqS[s[L]] == freqT[s[L]]:
                   numMatches -= 1 
                freqS[s[L]] -= 1
                L += 1

        return s[minL:minR+1] if minLength < float("inf") else ""
        