class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L < R:
            #get to a valid character to compare on both sides
            while L < R and not s[L].isalnum():
                L += 1
            while R > L and not s[R].isalnum():
                R -= 1
            
            #compare
            if s[L].lower() != s[R].lower():
               return False
            
            #iterate to next
            L += 1
            R -= 1
                    
        return True

            
                    