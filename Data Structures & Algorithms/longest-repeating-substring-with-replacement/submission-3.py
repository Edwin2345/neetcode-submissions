class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #slide widow, and kepe map of freq of chars in the window
        #valid while window_lenght -  max(freqMap.count()) <= k -> if so mupdate max
        #else, shrink from lef tuntil valid

        maxLenght = 0
        L=0
        R=0
        freqMap = {}

        while R < len(s):
            #update current char in freqmap
            if not s[R] in freqMap:
                freqMap[s[R]] = 1
            else:
                freqMap[s[R]] += 1
        
            #if invalid window (more unique chars than replacement), shrink from left            
            windowLenght = R - L + 1                        
            while windowLenght - max(freqMap.values()) > k:
                freqMap[s[L]] -= 1
                L += 1
                windowLenght = R - L + 1

            #compute window length
            maxLenght = max(maxLenght, windowLenght)

            #grow window
            R += 1
            


        return maxLenght