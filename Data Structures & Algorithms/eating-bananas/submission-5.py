class Solution:
    #P: need a function to calc total eating hours at rate k
    #P: we can use binary searhc of the number of hours is bimodal -> always <= h then filps to > h 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         #helpr function to calc total hours of eating at rate k
         def calcTotalHours(k):   
            totalHours = 0
            for p in piles:
               totalHours += p//k + 1 if p%k != 0 else p/k
            return totalHours
         
         L = 1
         R = max(piles)
         minK = R
         while L <= R:
            midK = L + (R - L) // 2
            totalHours = calcTotalHours(midK)
            #found a good enough value of k, try to make smaller
            if totalHours <= h:
               minK = min(minK, midK)
               R = midK - 1
            #otherwise search for a larger rate
            else:
               L = midK + 1
         
         return minK
        