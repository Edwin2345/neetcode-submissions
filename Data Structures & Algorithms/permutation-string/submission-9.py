class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #base case: s2 is smaller s1
        if len(s2) < len(s1):
           return False
        
        #freq count chars in s1
        s1Map = defaultdict(int)
        for ch in s1:
            s1Map[ch] += 1

        #slide window through s2
        s2Map = defaultdict(int)
        L, matches = 0, 0
        for R,ch in enumerate(s2):
            #if we are over the substr size, shrink from left until we can add
            while R-L+1 > len(s1):
                s2Map[s2[L]] -= 1
                if s2[L] in s1 and s2Map[s2[L]] + 1 == s1Map[s2[L]]:
                   matches -= 1 
                L += 1
            #add ch to substring -> check for perm
            s2Map[ch] += 1
            if ch in s1 and s2Map[ch] == s1Map[ch]:
               matches += 1
            if R-L+1 == len(s1) and matches == len(s1Map):
               return True 
             
        return False

