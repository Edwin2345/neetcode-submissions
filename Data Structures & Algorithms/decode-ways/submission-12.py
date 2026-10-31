class Solution:
    #any substring with leading 0 cna't be decoded
    #we can always decode a single digit if it begins with 1
    #we can decode a doubledign beging with 2 if 2nd digit is 0 to 6
    def numDecodings(self, s: str) -> int:
        validSecondDigits = set(["0","1","2","3","4","5","6"])

        #num ways to decode at i depends on i+1 and i+2 states
        #start with base case: if i > len(s), 0 ways to decode, i == len(s), 1 way to decode
        dp = [1,0]

        for i in range(len(s) - 1, -1, -1):
            #if i is "0" there are 0 ways, update dp states
            if s[i] == "0":
               tmp = dp[0]
               dp[0] = 0
               dp[1] = tmp 
            else:
               #add number of ways when decoding single digt
               curWays = dp[0]

               #add number of ways decoding 2 digis
               if i < len(s) -1 and (s[i] == "1" or s[i] == "2" and s[i+1] in validSecondDigits):
                  curWays += dp[1]
               
               #update dp states
               tmp = dp[0]
               dp[0] = curWays
               dp[1] = tmp
        
        return dp[0]
        