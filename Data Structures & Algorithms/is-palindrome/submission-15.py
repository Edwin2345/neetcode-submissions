class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isPal(L, R):
            #base case
            if L >= R:
               return True
            
            #skip non alphanumirc chars
            if not s[L].isalnum():
               return isPal(L+1,R)
            if not s[R].isalnum():
               return isPal(L,R-1)

            #not a palindrome
            if s[L].lower() != s[R].lower():
               return False 

            #iterate to next pair
            return isPal(L+1, R-1)


        return isPal(0,len(s)-1) 