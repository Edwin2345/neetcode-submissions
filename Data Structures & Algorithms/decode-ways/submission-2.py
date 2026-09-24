class Solution:
    def numDecodings(self, s: str) -> int:
       
        cache = {}
        def countDecodings(index):
            #decoded entire string successfully -> found 1 way
            if index >= len(s):
               return 1
            #unable to decode string as can't generate a letter from a number begining with 0
            if s[index] == "0":
               return 0
            #already compute total num ways to decode from this decision index
            if index in cache:
               return cache[index]

            #count ways when decoding a single digit number at this index
            totalNumWays = countDecodings(index + 1)

            #count ways when decoding a two digit number at this index if possible
            if index >= len(s) - 1:
               return totalNumWays 
            if s[index] == "1" or (s[index] == "2" and s[index+1] in "0123456"):
               totalNumWays += countDecodings(index + 2)
            
            #cache the result
            cache[index] = totalNumWays
            return cache[index]
        
        return countDecodings(0)