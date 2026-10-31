class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #bottom up
        #work backwords and see whcih words you break
        #can break entire string if dp[0] = True
        dp = [False]*(len(s) + 1)

        #base case: assume you can break entire word
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                #check if can break word to a future succesful state
                # if so move dp[i] to True aswell
                if i + len(word) > len(s):
                   continue
                if s[i : i + len(word)] == word and dp[i + len(word)] == True:
                   dp[i] = True
        
        #check if enitre word breakable
        return dp[0]
        
        

