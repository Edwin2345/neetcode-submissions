class Solution:
   #brutre force recurseion -> O(n*2^N) for the cost of slicing
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:        
        #put it in a set for o(1) lookup
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
        
        cache = {}
        def canBreakString(i):
            #fully broke down string
            if i == len(s):
               return True
            if i in cache:
               return cache[i] 

            #at current i try to find a substring s.t we can break off a word
            # check if we do that is the enitre rest of string also brekabale
            for word in wordSet:
                if s[i : i + len(word)] == word and canBreakString(i + len(word)):
                   cache[i] = True
                   return cache[i]
            
            #can't break string down
            cache[i] = False
            return cache[i]
        
        return canBreakString(0)      
            