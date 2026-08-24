class Solution:
    #iterate through tem[ps
    #add (temp, indx) to stack if smaller than top
    #once found larger temp, pop from stack, update with indices distance
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        daysUntilHotter = [0]*len(temperatures)
        stack = [ (temperatures[0], 0) ]

        for i in range(1,len(temperatures)):
            #once found hotter day, pop from stack and update
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                _ , j = stack.pop() 
                daysUntilHotter[j] = i-j

            #add current temp to stack
            stack.append( (temperatures[i], i) ) 
        
        return daysUntilHotter
        
        