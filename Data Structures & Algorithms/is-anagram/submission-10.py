class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = {}
        tCount = {}

        #Count frequencies
        for i in range(len(s)):
            sCount[s[i]] = sCount[s[i]]+1 if s[i] in sCount else 1
            tCount[t[i]] = tCount[t[i]]+1 if t[i] in tCount else 1
        
        #Check if frequncies are equal
        for i in range(len(s)):
            if (s[i] not in tCount) or (sCount[s[i]] != tCount[s[i]]):
                return False
        
        return True
        