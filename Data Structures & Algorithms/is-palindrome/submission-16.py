class Solution:
    #use two points at both ends
    #shrink towards middle, and skip until an alphanumeirc character appears
    #case insensitive
    #O(N) time O(1) space
    def isPalindrome(self, s: str) -> bool:
        L, R  = 0, len(s) - 1

        while L < R:
            #skip to alphumeric chare
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1

            #case insensitve compare
            if s[L].lower() != s[R].lower():
               return False 
            
            #go to next pair
            L += 1
            R -= 1

        return True
        