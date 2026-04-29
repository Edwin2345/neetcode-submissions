class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countT = {}
        countS = {}

        for i in range(len(s)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
            countS[s[i]] = 1 + countS.get(s[i], 0)

        for key, val in countS.items():
           if( countT.get(key,0) != val):
             return False
        return True