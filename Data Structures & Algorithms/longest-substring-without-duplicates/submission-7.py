class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #slidign window, grow window while possible, if found duplicate, shrink windwo until can add
        #o(n) time, at most o(n) space -> entire string unique
        windowSet = set()
        L = 0
        R = 0
        maxSubstringSize = 0
        while R < len(s):
            #try to add current to window, otherwsie, shift pop left side of window, then add
            if s[R] not in windowSet:
                 windowSet.add(s[R])
            else:
                while L <= R and s[R] in windowSet:
                    windowSet.remove(s[L])
                    L += 1
                windowSet.add(s[R])
            #compute substring size and shift window
            maxSubstringSize = max(maxSubstringSize, R-L+1)
            R += 1
        
        return maxSubstringSize
