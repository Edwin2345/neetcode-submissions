class Solution:
    #need to make fucntion to calc total shipment days
    # note: one foudn one valid capacity, any larger will also be valid
    # range we need to search is cpacity of max(weight) (n day shipping) to sum(weights) (1 day shipping)
    # edge cases: wieght >= 1 and days is at least 1 (so for some value it woudl work)
    #O(N*log(S)) where N is number of Weights, adn S is sum of weights TC, O(1) SC
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #O(N)
        def calcTotalShippingDays(boatCapacity):
            totalDays = 1
            shipWeight = 0
            for w in weights:
                #add on weights until capacity reached
                if shipWeight + w <= boatCapacity:
                   shipWeight += w
                #otehrwise, ship current weight for next day
                #weight will always fit as searching from max weight onwards
                else:
                   totalDays += 1
                   shipWeight = w
            return totalDays 
        
        #binary search a range from max(weight) to sum(weights)
        # O(log(S)) where S = sum(Weights)
        minCap, maxCap = max(weights), sum(weights)
        minValidCapacity = maxCap
        while minCap <= maxCap:
              cap = minCap + (maxCap - minCap) // 2
              #found valid capacity, try to make iut smaller bvy searchign smaller halve
              if calcTotalShippingDays(cap) <= days:
                 minValidCapacity = min(minValidCapacity, cap)
                 maxCap = cap - 1
              #capaicty too small, search upper half
              else:
                 minCap = cap + 1             
               
        return minValidCapacity

        