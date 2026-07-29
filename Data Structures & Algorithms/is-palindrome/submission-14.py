class Solution:
    #P: use two pointers to start at both ends
    #P: skip until you get a alphanumeric char, and compare with toLower
    def isPalindrome(self, s: str) -> bool:
        #base case: empty string
        if len(s) == 0:
           return True 
        
        L, R = 0, len(s)-1
        while L < R:
            #skip non alpnumir chars
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1
            
            #check if palindrome
            if s[L].lower() != s[R].lower():
               return False
            
            #iterate to next
            L += 1
            R -= 1

        return True 