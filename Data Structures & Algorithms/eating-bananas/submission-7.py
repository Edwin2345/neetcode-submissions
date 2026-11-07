class Solution:
    # you eat bannas at rate k per hour, but can't move to new pile until 1 horu passed
    # bananas in pile is >= 1
    # for each pile, the time to eat: if piles[i] % k == 0: piles[i] // k, else piles[i] // k + 1
    #solution 1, linear search k

    #TC: O(N*log(M)) as calcTotalEatTime is O(N) and it binayr searches through a range of 1 to M
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calcTotalEatTime(hourlyEatRate):
            totalTime = 0
            for numBananas in piles:
                if numBananas % hourlyEatRate == 0:
                   totalTime += numBananas // hourlyEatRate
                else:
                   #add 1 extra hour if not evenly divisible (smallest time unit) 
                   totalTime += numBananas // hourlyEatRate + 1 
            return totalTime

        #binary search to find min eating time
        # once we found a K that finishes in <= h hours, any large K will owkr awell
        minK, maxK = 1, max(piles)
        minValidK = float("inf")
        while minK <= maxK:
            k = minK + (maxK - minK) // 2
            #found a value of k that works, maxK has to at least be here
            if calcTotalEatTime(k) <= h:
               minValidK = min(minValidK, k)
               maxK = k - 1
            #otherwise, we need to find a higher k
            else:
               minK = k + 1   
        
        return minValidK

        