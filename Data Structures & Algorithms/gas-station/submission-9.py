class Solution:
    #circular route, at most one solution
    #Optimiziaiton, try to do it in a single pass wihtout looping
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #can't complete, else exactly one soluiton
        if sum(gas) < sum(cost):
           return -1 
     
        #now we can just do a linear scan from 1st to lasdt index, checking if any can be start
        startIndex = 0
        tank = 0
        
        for i in range(len(gas)):
            #if cant reach next, make the enxt index the start and reset tank
            if tank + (gas[i] - cost[i]) < 0:
               startIndex = i + 1
               tank = 0
            #otherwise update tank
            else:
               tank += (gas[i] - cost[i])  

        return startIndex
        