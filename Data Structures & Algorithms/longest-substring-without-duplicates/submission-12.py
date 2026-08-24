class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowSet = set()
        L = 0
        maxSubStrLen = 0
        for R,ch in enumerate(s):
            #shift window from left until can add right
            while ch in windowSet:
                windowSet.remove(s[L])
                L += 1
            #add new char and calc lenght of substrng
            windowSet.add(ch)
            maxSubStrLen = max(maxSubStrLen, R-L+1)

        return maxSubStrLen