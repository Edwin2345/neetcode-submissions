class Solution:
   #brutre force recurseion -> O(n*2^N) for the cost of slicing
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:        
        #put it in a set for o(1) lookup
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
        
        cache = {}
        def canBreakString(i):
            #was able to break up entire string
            if i == len(s):
               return True
            if i in cache:
               return cache[i] 

            #otherwise, find a substring that is in dict and see 
            #if passed that idnex we can break the full stirng
            for j in range(i, len(s)):
                if s[i:j+1] in wordSet and canBreakString(j+1):
                   cache[i] = True
                   return cache[i] 

            cache[i] = False
            return cache[i]
        
        return canBreakString(0)      
            