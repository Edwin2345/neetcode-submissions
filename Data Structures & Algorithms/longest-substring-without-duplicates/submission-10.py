class Solution:   
    #P: iterate throguh chars, If duplicate, pop from left pointer until can insert
    #P: Add right pointer char and Calc distance for both cases, keep a max vairable
    # Time Compelxity: O(s) -> iterate throguh string
    # Space Complexity: O(s) -> set at most store the entire string lenght
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        wordSet = set()
        L = 0
        for R in range(len(s)):  
            #add from right if not rempet
            if s[R] not in wordSet:
               wordSet.add(s[R])            
            #lelse shfit from left until can add
            else:
                while s[R] in wordSet:
                    wordSet.remove( s[L] )
                    L += 1
                wordSet.add( s[R] )

            #calc length
            maxLength = max(maxLength, R-L+1)         

        return maxLength