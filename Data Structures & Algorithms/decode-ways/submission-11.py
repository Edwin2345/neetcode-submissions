class Solution:
    #any substring with leading 0 cna't be decoded
    #we can always decode a single digit if it begins with 1
    #we can decode a doubledign beging with 2 if 2nd digit is 0 to 6
    def numDecodings(self, s: str) -> int:
        validSecondDigits = set(["0","1","2","3","4","5","6"])
        cache = {}
        def countDecodings(i):
            #successfully decoded entire string
            if i == len(s):
               return 1
            #can't decode because string begins with 0
            if s[i] == "0":
               return 0 
            #already computed num decodign ways starting form this index
            if i in cache:
               return cache[i] 

            #decode the single digit only
            numDecodings = 0  
            numDecodings += countDecodings(i + 1)

            #decode two digits if applicable
            if i <= len(s) - 2 and ((s[i] == "1") or (s[i] == "2" and s[i+1] in validSecondDigits)):
               numDecodings += countDecodings(i+2) 

            cache[i] = numDecodings
            return cache[i]
        
        return countDecodings(0)
        