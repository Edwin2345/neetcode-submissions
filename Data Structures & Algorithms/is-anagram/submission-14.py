#Q: Onyl lowercase letters?
#P: if strings are nto equal length -> rearily return false
#P: use freq map to store conts of s
#P: iterate throguh t
#   1. if char of t not in s -> false
#   2. if matching char in mapo -> decrment
#                                -> if coutn is zeor, remove from map
# check that len map == 0 at end
# Space Optimizaiton: use int26 arr, and match counter
# Time: O(s+t), Space: O(s)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if lenghts not equal -> def not anagram
        if len(s) != len(t):
           return False

        #build freqMap of s
        freqMap = {}
        for ch in s:
            if ch not in freqMap:
               freqMap[ch] = 1
            else:
               freqMap[ch] += 1
        
        #compare with t
        for ch in t:
            if ch not in freqMap:
               return False
            freqMap[ch] -= 1
            if freqMap[ch] == 0:
                freqMap.pop(ch)

        return len(freqMap) == 0


            

        
       