class Solution:
    #keep 2 pointers for both ends of substring
    #increase the subtring lenght while no repeat (use set ot check)
    #if duplicate found, start shrinkin substrign from left until you can ad dnew letter
    #O(N) TC as single scan, O(N) space for set
    def lengthOfLongestSubstring(self, s: str) -> int:
        letterSet = set()
        maxSubstringLen = 0
        L = 0
        for R in range(len(s)):
            #shirnk widnwo until we are able to add current letter
            while s[R] in letterSet:
                letterSet.remove( s[L] )
                L += 1
                
            letterSet.add( s[R] )

            #update max substirgn len
            maxSubstringLen = max(maxSubstringLen, R-L+1)

        return maxSubstringLen

        