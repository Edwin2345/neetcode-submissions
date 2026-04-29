class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowSet = set()
        L = 0
        maxLength = 0
        for R in range(len(s)):
            #grow sliding window while there is no duplicates
            if s[R] not in windowSet:
                windowSet.add(s[R])               
            #otherwise, shift L until inserting R is possible
            else:
                while(s[R] in windowSet):
                    windowSet.remove(s[L])
                    L += 1
                windowSet.add(s[R])
            
            maxLength = max(maxLength, R-L+1)
                     
        return maxLength