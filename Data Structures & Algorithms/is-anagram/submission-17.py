class Solution:
    # only lowercase letters,anagram = same freq but possibly diff order
    # O(n) TC, O(1) space for freq map as both max size of 26
    def isAnagram(self, s: str, t: str) -> bool:
        #if strigns not smae
        if len(s) != len(t):
           return False

        #freq count the letters
        sFreq, tFreq = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            sFreq[s[i]] += 1
            tFreq[t[i]] += 1
        
        #see if counts match
        for letter in s:
            if letter not in tFreq:
               return False
            elif sFreq[letter] != tFreq[letter]:
               return False 

        return True
        


        
        