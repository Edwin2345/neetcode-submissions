class Solution:
    #P: freq count t and create zero intial freq map for s
    #P: grow window until matchCount = len(t) (onyl incrmenet whenf req match exactly)
    #P: once we have a match - check if min, then start shrinking from left
    #P: as soon as matchCOunt < len(t) -> grow from right again until we match
    def minWindow(self, s: str, t: str) -> str:
        minWindowStr = ""
        minLength = float("inf")

        #if s is smaller than t -> no match possible
        if len(s) < len(t):
           return "" 

        #create sMap and tMap
        sMap, tMap = defaultdict(int), defaultdict(int)
        for ch in t:
            tMap[ch] += 1

        matchCount = 0
        L=0
        for R in range(len(s)):            
            #grow window from the right
            sMap[s[R]] += 1
            if s[R] in tMap and sMap[s[R]] == tMap[s[R]]:
               matchCount += 1 

            #found a valid window
            while matchCount == len(tMap):
                # save result if min
                if matchCount == len(tMap) and (R-L+1) < minLength:
                   minLength = R-L+1
                   minWindowStr = s[L:R+1]
                
                #shrink window while it stil contians substring
                if s[L] in tMap and sMap[s[L]] - 1 < tMap[s[L]]:
                    matchCount -= 1
                sMap[s[L]] -= 1
                L += 1

        return minWindowStr
            
