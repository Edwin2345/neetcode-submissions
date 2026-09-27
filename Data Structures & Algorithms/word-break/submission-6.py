class Solution:
   # bottom up dp --> O(N * M * L) where N is len(s), M is number of words in dict, L is lenght of longest wor
   #              --> *L because we make a slice
   #              --> O(N + M) space for cache, dp state and wordSet
    def wordBreak(self, s: str, wordDict: List[strallstack]) -> bool:        
        #put it in a set for o(1) lookup
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
        
        #have boolean dp array -> dp[i] = True iff substring starting at i 
        #is breakable
        dp = [False]*(len(s) + 1)

        #base case: after processing entry string -> empty string breakable
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            #we set cur index to true iff break off word, and dp[i + len(word)] = True
            for word in wordSet:
                if i + len(word) > len(s):
                   continue
                if s[i : i + len(word)] == word and dp[i + len(word)] == True:
                   dp[i] = dp[i + len(word)]  
        
        #return dp[0] -> checks if entie stirng is brekabale
        return dp[0]
 
            