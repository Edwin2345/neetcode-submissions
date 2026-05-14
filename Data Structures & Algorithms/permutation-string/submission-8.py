class Solution:
    #check if s1 is perm of s2
    #questiosns -> only lowercase letters?, is s1 size garentted to be less than s2
    def foundMatch(self, freqS1, curFreq):
        for i in range(26):
            if freqS1[i] != curFreq[i]:
               return False  
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        #if s1 larger than s2 -> not possible:
        if len(s1) > len(s2):
            return False

        #1. create a freq arr of s1
        freqS1 = [0]*26
        for l in s1:
            freqS1[ord(l)-ord('a')] += 1

        #3 build first fixed window fo size s1, check if amtch
        L = 0
        R = 0
        curFreq = [0]*26
        while R-L+1 <= len(s1):
            curFreq[ord(s2[R]) - ord('a')] += 1
            R += 1
        if self.foundMatch(freqS1, curFreq):
            return True

        #3. slide fixed window until match found
        while R < len(s2):
              #remove L, add R
              curFreq[ord(s2[L]) - ord('a')] -= 1
              curFreq[ord(s2[R]) - ord('a')] += 1

              #check if match found
              if self.foundMatch(freqS1, curFreq):
                return True

              #shift window
              L += 1
              R += 1

        return False
