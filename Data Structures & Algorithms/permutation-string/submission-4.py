class Solution:
    def compareFreq(self, c1, c2):
        for i in range(26):
            if c1[i] != c2[i]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        #if s1 larger than s2 -> not possible:
        if len(s1) > len(s2):
            return False
        
        #create two freq arr of characters in both string -> initial window size len(s1)
        countS1, countS2 = [0]*26, [0]*26
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1

        #check if inital window is palindrome
        if self.compareFreq(countS1, countS2):
            return True
        
        #else -> shift s2 window, adjust freq, and check if palindrome
        L=0
        for R in range(len(s1), len(s2)):          
            countS2[ord(s2[L]) - ord('a')] -= 1
            countS2[ord(s2[R]) - ord('a')] += 1
            L += 1
            if self.compareFreq(countS1, countS2):
                return True
        
        return False



