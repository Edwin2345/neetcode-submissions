class Solution:
   def numDecodings(self, s: str) -> int:
     #base cases: if at i > len(s) -> no way to decode, i == len(s) -> succ decoded 1 way
     dp = [1,0]

     for i in range(len(s)-1, -1, -1):
        #can't even decode single digit num
        if s[i] == "0":
           curWays = 0
        else:
           #add all the ways when you decode a signle digit here
           curWays = dp[0]
           # add all the double digit decode ways if applicable
           if i <= len(s) -2 and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
              curWays += dp[1]
 
        dp[1] = dp[0]
        dp[0] = curWays  
              
     return dp[0]