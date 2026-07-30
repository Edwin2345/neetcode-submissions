class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        windowSet = set()
        
        L = 0
        for R in range(len(s)):
            #grow window while you can
            if s[R] not in windowSet:
               windowSet.add(s[R]) 
            #otherwise, remove from left until you can add R
            else:
                while L < R and s[R] in windowSet:
                    windowSet.remove(s[L])
                    L += 1
                windowSet.add(s[R])
            
            #compute lenght of substring and updat max
            maxLen = max(maxLen, R-L+1)

        return maxLen