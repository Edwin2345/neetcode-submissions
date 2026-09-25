class Solution:
    def numDecodings(self, s: str) -> int:

      cache = {}  
      def countDecodings(index):
         #successfully decoded entire string
         if index >= len(s):
            return 1          
         #can't decode any further as number begins with '0'
         if s[index] == "0":
            return 0
         #already computed in num decodable ways for this index
         if index in cache:
            return cache[index]
         
         #count ways when decoding only a signle digiti numebr at this index
         totalWays = countDecodings(index + 1)

         #if possible to decode a 2 digit num at this index, add those ways aswel
         if index >= len(s) - 1:
            cache[index] = totalWays
            return cache[index]
         if (s[index] == "1") or (s[index] == "2" and s[index + 1] in "0123456"):
            totalWays += countDecodings(index + 2)
         
         cache[index] = totalWays
         return cache[index]
      
      return countDecodings(0)