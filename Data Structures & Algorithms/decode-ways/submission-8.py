class Solution:
    def numDecodings(self, s: str) -> int:

      #idea: we can use the num wyas from the next index and next next index
      #to find nuymebr fo ways at current index

      #base case -> if i > len(s) -> no ways to decode, 
      #          -> if i == len(s)  -> only 1 way to decode 
      dp = [1,0]
      curWays = 0
      for i in range(len(s)-1, -1, -1):         
          #current index is 0 -> don't update count at all
          if s[i] == "0": 
             curWays = 0
          else:
             #safe to add all the ways only decoding single digit at index
             curWays = dp[0]
             #add on num ways decoding double digit at thsi index
             if i <= len(s) -2 and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                curWays += dp[1]
          dp[1] = dp[0]
          dp[0] = curWays 
         
      return dp[0]