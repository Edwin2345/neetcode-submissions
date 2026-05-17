class Solution:
    def calcEatingTime(self, piles, k):
        totalHours = 0
        for p in piles:
            #if bannanis in pile les than eating rate, still need to spend 1 hour
            if p < k:
               totalHours += 1 
            #otherwise take the division rounded up if nbot wholly divisble 
            else:
               totalHours += (p // k + 1) if p%k != 0 else p // k
        return totalHours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #we can use binary search to find k to fit atleast h
        L = 1
        R = max(piles)
        minK = R

        while L <= R:
           #use midpoint of range to find eating time 
           mid = L + (R-L) // 2
           eatingTime = self.calcEatingTime(piles, mid)  

           #if valid time, record but try to shrink window
           if eatingTime <= h:
              minK = min(minK, mid)
              R = mid - 1
           #otherwise, nee dto search uper half of range   
           else:
              L = mid + 1

        return minK
        