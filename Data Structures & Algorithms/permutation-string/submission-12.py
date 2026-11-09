class Solution:
    #O(N+M) TC as linear scan of both strings, s1 and s2 O(S+T) space where S,T are numebr fo unqiue characters in s1 and s2
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #a substrign perm is not pssble if s1 is alrady bigger
        if len(s1) > len(s2):
           return False 
        
        #buildFreqMap of s1
        s1Freq = defaultdict(int)
        for letter in s1:
            s1Freq[letter] += 1

        #slide fixed size window of len(s1) across s2
        s2Freq = defaultdict(int)
        L, matches = 0,0
        for R in range(len(s2)):
            #shrink substring from left until you can add letter at R
            while R-L+1 > len(s1):
                #update matches if applicable
                if s2[L] in s1Freq and s1Freq[s2[L]] == s2Freq[s2[L]]:
                   matches -= 1
                s2Freq[s2[L]] -= 1
                L += 1
            
            #add R and update matches if applicable
            s2Freq[s2[R]] += 1
            if s2[R] in s1Freq and s1Freq[s2[R]] == s2Freq[s2[R]]:
               matches += 1

            #see if found valid and go to next iteration
            if matches == len(s1Freq):
               print(s2[L:R+1])
               return True 

        return False 