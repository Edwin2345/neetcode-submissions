class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #can't compelte circuit no matter what
        if sum(gas) < sum(cost):
           return -1

        #start with empty tank adn try starting at index 1
        tank = 0
        startIndex = 0 
        for i in range(len(gas)):
            #caulate the surplus gas you have after fuel and tavelign to i+1 station
            tank += (gas[i] - cost[i])

            #if you tank is empty, not possible to rech next station, must start later
            if tank < 0:
               startIndex = i + 1
               tank = 0 
        
        return startIndex

