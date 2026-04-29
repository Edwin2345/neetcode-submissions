class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowSet = set()
        L = 0
        maxLength = 0
        for R in range(len(s)):
            #if R in set alread, shift window until can insert
            while(R < len(s) and s[R] in windowSet):
                windowSet.remove(s[L])
                L += 1
            #add to window and update maxLength
            windowSet.add(s[R])
            if R-L+1 > maxLength:
               maxLength = R-L+1

        return maxLength