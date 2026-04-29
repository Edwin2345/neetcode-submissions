class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Intuition --> keep a stack of decreasing temps, 
                      and once found once higher then last recent, pop and compute diff


        tmp    30,38,30,36,35,40
        stck   (38,1),(30,2) --> 36,3 
               (38,1),(36,3),(35,4) --> 40,5 
        '''
        #default to no days higher
        res = [0]*len(temperatures)
        stack = []


        for i,t in enumerate(temperatures):
            #keep stack in decreasing order
            if len(stack) == 0 or stack[-1][0] >= t:
                stack.append([t,i])
            #found a higher later temp -> compute diff while possible and add to stack once done
            else:
                while(len(stack) and stack[-1][0] < t):
                    #compute index diff as number of days hotter
                    res[stack[-1][1]] = i-stack[-1][1]
                    stack.pop()
                stack.append([t,i])
        
        return res




                
        

        return res