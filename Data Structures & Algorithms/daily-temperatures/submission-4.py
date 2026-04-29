class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #o(n) solution -> use stack in decreaing order, then once found higher, you can 
        result = [0]*len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            #keep a stack in decreasing order
            if len(stack) == 0 or stack[-1][0] >= t:
               stack.append([t,i])
            #found a hotter day than the top of stack -> compute results while possible then add to stack
            else:
                while(stack and stack[-1][0] < t):
                    d,j = stack.pop()
                    result[j] = i-j 
                stack.append([t,i])
        
        return result
                


        
        
        return result