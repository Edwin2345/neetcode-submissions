class Solution:
    def checkLetterFreq(self, s1Freq, s2Freq):
        for i in range(26):
            if s1Freq[i] != s2Freq[i]:
               return False
        return True 

    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge case -> permutation longer than string
        if len(s1) > len(s2):
           False

        s1Freq = [0]*26  
        s2Freq = [0]*26   

        #build freq counter for s1
        for ch in s1:
            s1Freq[ord(ch)-ord('a')] += 1
       
        #check every sliding window of size len(s1)
        K = len(s1)
        L = 0
        for R in range(len(s2)):
            #add current char
            s2Freq[ord(s2[R]) - ord('a')] += 1
            #if current string of length k -> check then shift
            if(R-L+1 == K):
                if self.checkLetterFreq(s1Freq,s2Freq):
                    print(s2[L:R+1])
                    return True
                #shift L up 1
                s2Freq[ord(s2[L]) - ord('a')] -= 1
                L += 1

        #no valid sliding window found
        return False

        