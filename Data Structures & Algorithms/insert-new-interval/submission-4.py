class Solution:
    #insert newInterval by lookign at the start time (as intervals initally sorted)
    #then run merge algo
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #base case: empty interval list
        if len(intervals) == 0:
           return [newInterval] 
      
        #insert at correct spot using lower bound binary search
        L, R = 0, len(intervals) #--> as we cna insert at start and end
        while L < R:
            M = L + (R-L)//2
            if newInterval[0] <= intervals[M][0]:
               R = M
            else:
               L = M + 1

        intervals.insert(L, newInterval)
          
        #merge overlapping intervals
        mergedIntervals = []
        i = 0
        while i < len(intervals):
            curStartTime, curEndTime = intervals[i][0], intervals[i][1]

            j = i + 1
            while j < len(intervals) and curEndTime >= intervals[j][0]:
                  curEndTime = max(curEndTime, intervals[j][1])
                  j += 1
            
            mergedIntervals.append([curStartTime, curEndTime])
            i = j

        return mergedIntervals
        

