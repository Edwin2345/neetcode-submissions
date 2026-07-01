class Solution:
    #keep a map of freq of both window and t
    #keep a vairable fo numebr of matchs, increment as soon as freq_s = freq_t for a char
    #once match found -> repeatedly compute min window and try to pop from left until matchNum drops
    def minWindow(self, s: str, t: str) -> str:
        #coutner variables
        minLength = float("inf")
        minStringStart = -1
        minStringEnd = -1
        
        #calc freq of t
        tMap = defaultdict(int)
        for ch in t:
            tMap[ch] += 1
        
        #slide window
        L=0
        sMap = defaultdict(int)
        matchCount = 0
        for R in range(len(s)):
            #grow window until we have match
            if matchCount < len(tMap):
               sMap[s[R]] += 1
               if s[R] in tMap and sMap[s[R]] == tMap[s[R]]:
                  matchCount += 1

            #repeatly try to shrink window from left while sitll matching
            while matchCount == len(tMap):
                #found new min string
                if minLength > R-L+1:
                   minLength = R-L+1
                   minStringStart = L
                   minStringEnd = R 

                #shrink from left
                sMap[s[L]] -= 1
                if s[L] in tMap and sMap[s[L]] < tMap[s[L]]:
                   matchCount -= 1 
                L += 1
        
        return s[minStringStart : minStringEnd + 1]

        