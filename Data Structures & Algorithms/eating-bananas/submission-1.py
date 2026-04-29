class Solution:
    '''
    min eating rate -> 1, max eating rate = max(piles) -> takes len(piles) 
    once found a k value that works -> any higher k value will also -> first bad version type problem
    '''
    def computeTotalHours(self, piles, k):
        totalHours = 0
        for p in piles:
            if k >= p:
                totalHours += 1
            elif p%k != 0:
                totalHours += p//k + 1 
            else:
                totalHours += p//k 
        return totalHours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowK = 1
        highK = max(piles)
        
        while(lowK < highK):
            midK = lowK + (highK-lowK)//2
            #if all eating before h -> high can be atleast this k value
            if(self.computeTotalHours(piles,midK) <= h):
                highK = midK            
            #not meeting time req -> increase k
            else:
                lowK = midK+1

        #min K value occurs where low and high converge
        return lowK