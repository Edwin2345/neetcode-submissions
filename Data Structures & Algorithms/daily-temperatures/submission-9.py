class Solution:
    #result[i] --> number of days after until strictly warmer
    #need to keep track of previous seen temps -> list or stack
    #keep popping form stakc while current temp is hotter than top, then push current temp onto stack (both the temp and idnex)
    #stack is basically stores previous temps in decreasing order

    #O(N) time (single pass) and O(N) space
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i, tmp in enumerate(temperatures):
            #keep popping from stack and updating results while current temp > top
            while len(stack) > 0 and temperatures[stack[-1]] < tmp:
                  oldTmpIndex = stack.pop()
                  result[oldTmpIndex] = i - oldTmpIndex
            
            #add current index to stack to be processed in future
            stack.append( i )
        
        return result

        