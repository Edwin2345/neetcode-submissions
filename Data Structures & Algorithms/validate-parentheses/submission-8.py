class Solution:
   def isValid(self, s: str) -> bool:
      n = len(s)
      open_brac = []

      if n%2==1:
         return False
      
      for string in s:
         if (string == ')' or string == ']' or string == '}') and len(open_brac) == 0:
            return False

         if string == ')':
            if open_brac.pop() != '(':
               return False
         
         elif string == ']':
            if open_brac.pop() != '[':
               return False
         
         elif string == '}':
            if open_brac.pop() != '{':
               return False
         
         else:
            open_brac.append(string)

      return len(open_brac) == 0
         