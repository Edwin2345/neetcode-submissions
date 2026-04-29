class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        maxLength = 0
        seen = set()
        for R in range(len(s)):
            if s[R] in seen:
               while(s[R] in seen):
                 seen.remove(s[L])
                 L+=1
               seen.add(s[R])
            else: 
               seen.add(s[R])
            
            maxLength = max(maxLength, R-L+1)     
            
        return maxLength