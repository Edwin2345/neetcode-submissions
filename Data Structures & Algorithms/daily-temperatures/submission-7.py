class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #O(N) time, O(N) spac,e use a montoic decreasing stakc of temps
        #once found temp larger than top of stack (smallest prev day temp value), pop and update daysTill hotter

        daysTillHotter = [0]*len(temperatures)
        prevTempStack = []

        for i,t in enumerate(temperatures):
            if len(prevTempStack) == 0 or t <= prevTempStack[-1][0]:
               prevTempStack.append( (t,i) )
            else:
                while len(prevTempStack) > 0 and t > prevTempStack[-1][0]:
                    _ , prevTempIndex = prevTempStack.pop()
                    daysTillHotter[prevTempIndex] = i - prevTempIndex
                
                #add cur temp as it is <= than prev days lef tin stacj
                prevTempStack.append( (t,i) )
        
        return daysTillHotter