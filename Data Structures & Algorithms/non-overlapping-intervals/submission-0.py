class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
       #base case, -> not intervals
       if not intervals:
          return 0

       #sort by start times
       intervals.sort()

       #compare prevEnd with curStart for overlap detection
       prevEnd = intervals[0][1]
       removeCnt = 0
       for i in range(1, len(intervals)):
           curStart, curEnd  = intervals[i][0], intervals[i][1]

           #overlap detected, remove the interval that ends later
           #as less chance of overlappign with subsequent intervals
           if prevEnd > curStart:
              removeCnt += 1
              prevEnd = min(prevEnd, curEnd) #effectively removing later interval
           #no overlap, shift prevEnd over
           else:
              prevEnd = curEnd
        
       return removeCnt
              
            
        
