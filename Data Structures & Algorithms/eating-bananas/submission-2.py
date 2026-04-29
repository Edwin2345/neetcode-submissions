class Solution:
    def calculateEatingHours(self, piles, k):
        hours = 0
        for p in piles:
            if(p % k == 0):
                hours += p // k
            else:
                hours += p // k + 1
        return hours


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #lower bound on rate -> 1 per hour
        L = 1
        #upper bound on rate -> largest pile
        U = max(piles)

        #binary search to find min eating rate (k)
        while(L < U):
            k = L + (U-L)//2
            hours = self.calculateEatingHours(piles,k)
            #found an apporiate k -> rate has to atleast be this large
            if hours <= h:
                U = k
            #k value too small, move lower bound up
            else:
                L = k+1
        
        #min rate is where lower and upper bound converge
        return L
        


        