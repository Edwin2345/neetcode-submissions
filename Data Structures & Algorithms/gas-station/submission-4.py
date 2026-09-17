class Solution:
    #O(N) -> look at sum of total gas to totoal cost + net gas after each station
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # not enoguh gas to pay full cost
        if sum(gas) < sum(cost):
           return -1

        #start you tank with 0, tryt first index as the start
        startIndex, tank =  0, 0 
        for i in range(len(gas)):
            #add net gas you get after passtng current indiex
            tank += (gas[i] - cost[i])

            #if tank < 0, we can't move to enxt station -> move start to i+1
            # we skip al values between startIndex and I becuase even with
            # the extra net gas we got form station startIndex, it wan't enough
            if tank < 0:
               startIndex = i + 1
               tank = 0
        
        #return startIndex as the valid starting point
        #we only needed to check if can reach last sation because we know from
        #1st check there HAS to be a gas surplus in total
        #all previous indice up to startIndex failed as they put us in gas definit
        #the remainign statiosn must put us in a suplus to equal global toal suplus
        #the startIndex we foudn was the beiging of this suplus section > decifict section
        return startIndex