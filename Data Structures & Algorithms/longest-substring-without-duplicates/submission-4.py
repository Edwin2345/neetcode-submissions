class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        maxLength = 0
        for R in range(len(s)):
            #grow window while no dupes:
            if(s[R] not in window):
                window.add(s[R])
            #else if duplicate, shift and pop window until can insert
            else:
                while(L < R and s[R] in window):
                    window.remove(s[L])
                    L += 1
                window.add(s[R])

            #evaluate max length
            maxLength = max(maxLength, len(window))
        
        return maxLength